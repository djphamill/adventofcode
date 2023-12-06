from math import inf
import re
import sys
import time
from typing import Dict, List, Tuple, Callable, Iterator, Union

def get_destination(source: int, map: Dict[tuple, tuple]) -> int:
    destination = source
    for key in map:
        start_of_key, end_of_key = [k for k in iter(key)]
        if start_of_key <= source <= end_of_key:
            index = source - start_of_key
            start_destination = map[key][0]
            destination = start_destination + index
            break
    return destination

def build_map(lines: List[str]) -> Tuple[str, str, Dict[tuple, tuple]]:
    source_field, destination_field = lines[0].replace('map:', '').strip().split('-to-')
    map = {}
    for line in lines[1:]:
        destination_start, source_start, range= [int(n) for n in line.split(' ')]
        source_range = tuple([source_start, source_start + range - 1])
        destination_range = tuple([destination_start, destination_start + range - 1])
        map.update({source_range: destination_range})
    return source_field, destination_field, map

def get_map_lines(lines: List[str]) -> List[List[str]]:
    lines_without_seeds = lines[2:]
    map_lines = []
    map_section = []
    for line in lines_without_seeds:
        if not line and map_section:
            map_lines.append(map_section)
            map_section = []
            continue
        map_section.append(line)
    map_lines.append(map_section)
    return map_lines

def get_seeds(lines: List[str]) -> List[int]:
    return [int(seed.strip()) for seed in lines[0].replace("seeds:", "").strip().split(' ')]

def pt1(lines):
    return find_lowest_seed_location(lines, get_seeds)

def find_lowest_seed_location(lines: List[str], seed_getter: Callable) -> int:
    maps = build_maps(lines)

    seeds = seed_getter(lines)
    lowest_location = inf
    for seed in seeds:
        source = seed
        for map in maps:
            destination = get_destination(source, map)
            source = destination
        if destination < lowest_location:
            lowest_location = destination
    return lowest_location

def build_maps(lines) -> List[Dict[tuple, tuple]]:
    map_lines = get_map_lines(lines)
    maps = []
    if [] in map_lines:
        print(f'empty string in {map_lines}')
    for map_seciton_lines in map_lines:
        source, destination, map = build_map(map_seciton_lines)
        maps.append(map)
    return maps

def get_seeds_with_ranges(lines: List[str]) -> Iterator[int]:
    number_line = lines[0].replace("seeds:", "").strip()

    seed_pair_pattern = r'\d+\s\d+'
    matches = re.findall(seed_pair_pattern, number_line)
    for match in matches:
        start_number, amount_to_add = [int(n) for n in match.split(' ')]
        for i in range(amount_to_add):
            yield start_number + i

def pt2(lines: List[str], holder: List[Union[None, int]] = None, index: int = None):
    lowest_location = find_lowest_seed_location(lines, get_seeds_with_ranges)
    if holder and index:
        holder[index] = lowest_location
    return lowest_location

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