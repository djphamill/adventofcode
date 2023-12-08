import re 
import sys
import time
from typing import List, Dict, Tuple
from day05 import build_maps
from dataclasses import dataclass

@dataclass
class Range:
    start: int
    end: int


def pt1(lines: List[str]) -> str:
    return

def pt2(lines: List[str]) -> str:
    seeds_as_ranges = get_seeds_as_ranges(lines)
    maps = build_maps(lines)
    
    
    return

def get_seeds_as_ranges(lines: List[str]) -> List[int]:
    number_line = lines[0].replace("seeds:", "").strip()

    seeds = []
    seed_pair_pattern = r'\d+\s\d+'
    matches = re.findall(seed_pair_pattern, number_line)
    for match in matches:
        start_number, amount_to_add = [int(n) for n in match.split(' ')]
        seeds.append((start_number, amount_to_add))
    
    return seeds       
    
def get_destination_of_first_range(source_range: Tuple[int], map: Dict[tuple, tuple]) -> Tuple[Tuple[int]]:
    first_destination_range = tuple()
    remaining_source_range = tuple()
    
    starting_source = source_range[0]
    for mapped_source_range in map:
        mapped_source_range = range(**mapped_source_range)
        if starting_source not in mapped_source_range:
            continue
     
    return first_destination_range, remaining_source_range

def get_seed_to_soil_map(lines: List[str]):
    return

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    start = time.time()
    print(f'Part 1: {pt1(lines)}')
    end = time.time()
    print(f'Part 1 took {end - start}')
    
    start = time.time()
    print(f'Part 2: {pt2(lines)}')
    end = time.time()
    print(f'Part 2 took {end - start}')