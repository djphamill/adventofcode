# current_record = speed * (race_duraction - seconds_held)
# current_record = seconds_held * (race_duraction - seconds_held)
# current_record = seconds_held * race_duraction - seconds_held^2
# 0 = - seconds_held^2 + seconds_held * race_duration - current_record
# a = -1
# b = race_duration
# c = - current_record

from math import floor, ceil, sqrt
import re
import sys
import time
from dataclasses import dataclass
from typing import List, Union, Tuple

def pt1(lines: List[str]) -> Union[str, int]:
    total = 1
    races = get_races(lines)
    for race in races:
        number_of_ways_to_win = get_number_of_ways_to_win(race)
        total *= number_of_ways_to_win
        
    return total

def pt2(lines):
    for i in range(len(lines)):
        lines[i] = lines[i].replace(' ', '')
        
    return pt1(lines)

@dataclass
class Race:
    duration: int
    current_record: int

def get_races(lines: List[str]) -> List[Race]:
    times = re.findall(r"\d+", lines[0].replace('Time:', '').strip())
    distance_records =  re.findall(r"\d+", lines[1].replace('Distance:', '').strip())
    
    races = []
    for duration, current_record in zip(times, distance_records):
        races.append(Race(int(duration), int(current_record)))
        
    return races

def get_number_of_ways_to_win(race: Race) -> int:
    lower, upper = get_boundary_cases(race)
    first_value = floor(lower) + 1
    last_value = ceil(upper) - 1
    number_of_ways_to_win = last_value - first_value + 1
    return number_of_ways_to_win

def get_distance(milliseconds_held_for: int, race_duration: int) -> int:
    speed = milliseconds_held_for
    distance = speed * (race_duration - milliseconds_held_for)

    return distance

def quadratic_solver(a: int, b: int, c: int) -> Tuple[float]:
    discriminant = pow(b, 2) - 4*a*c
    first_solution = (-1*b - sqrt(discriminant)) / (2*a)
    second_solution = (-1*b + sqrt(discriminant)) / (2*a)
    solutions = [first_solution, second_solution]
    solutions.sort()
    return solutions

def get_boundary_cases(race: Race) -> Tuple[int]:
    a, b, c = -1, race.duration, -1*race.current_record
    boundaries = quadratic_solver(a, b, c)
    
    return boundaries

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')

    start = time.time()
    print('=' * 10)
    print(f'Part 1: {pt1(lines)}')
    end = time.time()
    print('.' * 10)
    print(f'Part 1 took {end - start}')
    print('=' * 10)
    start = time.time()
    print(f'Part 2: {pt2(lines)}')
    end = time.time()
    print('.' * 10)
    print(f'Part 2 took {end - start}')
    print('=' * 10)