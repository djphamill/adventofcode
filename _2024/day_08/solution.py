"""
Solution to day 08
"""
from string import ascii_lowercase, ascii_uppercase, digits
from itertools import combinations
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict
from collections import defaultdict
from math import gcd

VALID_FREQUENCIES = ascii_lowercase + ascii_uppercase + digits

@dataclass
class Antenna:
    right: int
    down: int
    frequency: str

@dataclass
class Antinode:
    right: int
    down: int
    antennae: List[Antenna]

class Antennae:
    
    def __init__(self):
        self._antennae = defaultdict(list)

    def add_antenna(self, antenna: Antenna) -> None:
        self._antennae[antenna.frequency].append(antenna)
    
    def with_frequency(self, frequency) -> "Antennae":
        return self._antennae[frequency]

def solution_part_01(input: str) -> str:
    map = [line.strip() for line in input.split('\n') if line]

    antennae = find_antennae(map)
    all_antinodes: List[Antinode] = []
    for freqency in VALID_FREQUENCIES:
        antennae_for_frequency = antennae.with_frequency(freqency)
        anitnodes_for_frequency = find_antinodes_at_two_one_ratio(map, antennae_for_frequency)
        all_antinodes.extend(anitnodes_for_frequency)
    
    distinct_locations = set((antinode.right, antinode.down) for antinode in all_antinodes)
    return str(len(distinct_locations))

def find_antennae(map: List[str]) -> Antennae:
    antennae = Antennae()
    for right, row in enumerate(map):
        for down, char in enumerate(row):
            if char in VALID_FREQUENCIES:
                antennae.add_antenna(Antenna(right, down, char))
            elif char != '.':
                raise Exception(f'Found char: {char}')
    
    return antennae

def find_antinodes_at_two_one_ratio(map: List[str], antennae: List[Antenna]) -> List[Antinode]:
    antinodes: List[Antinode] = []
    
    internal_antinodes = find_internal_antinodes(antennae)
    antinodes.extend(internal_antinodes)

    external_antinodes = find_external_antinodes(antennae, map)
    antinodes.extend(external_antinodes)

    return antinodes

def find_internal_antinodes(antennae: List[Antenna]) -> List[Antinode]:
    internal_antinodes: List[Antinode] = []
    pairs_of_antennae = combinations(antennae, 2)
    for a_1, a_2 in pairs_of_antennae:
        can_be_horizontally_trisected = (a_1.right - a_2.right) % 3 == 0
        can_be_vertically_trisected = (a_1.down - a_2.down) % 3 == 0
        if not can_be_horizontally_trisected or not can_be_vertically_trisected:
            continue
        
        for closer_antenna, further_antenna in [[a_1, a_2], [a_2, a_1]]:
            right = (2 * closer_antenna.right + further_antenna.right) / 3
            down = (2 * closer_antenna.down + further_antenna.down) / 3
            internal_antinodes.append(Antinode(right, down, [closer_antenna, further_antenna]))
    
    return internal_antinodes

def find_external_antinodes(antennae: List[Antenna], map: List[str]) -> List[Antinode]:
    external_antinodes: List [Antinode] = []
    pairs_of_antennae = combinations(antennae, 2)
    for a_1, a_2 in pairs_of_antennae:
        for closer_antenna, further_antenna in [[a_1, a_2], [a_2, a_1]]:
            right = (closer_antenna.right - further_antenna.right) * 2 + further_antenna.right
            down = (closer_antenna.down - further_antenna.down) * 2 + further_antenna.down
            antinode = Antinode(right, down, [closer_antenna, further_antenna])
            if is_outside_map(map, antinode):
                continue
            external_antinodes.append(antinode)
    
    return external_antinodes

def is_outside_map(map: List[str], antinode: Antinode) -> bool:
    return antinode.right < 0 or antinode.down < 0 or antinode.right >= len(map[0]) or antinode.down >= len(map)

def solution_part_02(input: str) -> str:
    map = [line.strip() for line in input.split('\n') if line]

    antennae = find_antennae(map)
    all_antinodes: List[Antinode] = []
    for freqency in VALID_FREQUENCIES:
        antennae_for_frequency = antennae.with_frequency(freqency)
        anitnodes_for_frequency = find_antinodes(map, antennae_for_frequency)
        all_antinodes.extend(anitnodes_for_frequency)
    
    distinct_locations = set((antinode.right, antinode.down) for antinode in all_antinodes)
    return str(len(distinct_locations))

def find_antinodes(map: List[str], antennae: Antennae) -> List[Antinode]:
    antinodes: List[Antinode] = []
    
    for antenna_pair in combinations(antennae, 2):
        antinodes_for_par = find_all_antinodes_for_pair(*antenna_pair, map)
        antinodes.extend(antinodes_for_par)

    return antinodes

def find_all_antinodes_for_pair(a_1: Antenna, a_2: Antenna, map: List[str]) -> List[Antinode]:
    antinodes: List[Antinode] = []
    for start, other in [[a_1, a_2], [a_2, a_1]]:
        gradient = find_gradient(start, other)
        step = 0
        while True:
            step +=1
            right = start.right + step * gradient.right
            down = start.down + step * gradient.down
            antinode = Antinode(right, down, [start, other])
            if is_outside_map(map, antinode):
                break
            antinodes.append(antinode)

    return antinodes

@dataclass
class Gradient:
    right: int
    down: int

def find_gradient(a: Antenna, b: Antenna) -> List[int]:
    right_delta = b.right - a.right
    down_delta = b.down - a.down
    divisor = gcd(right_delta, down_delta)
    return Gradient(int(right_delta / divisor), int(down_delta / divisor))