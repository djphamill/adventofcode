from day05 import pt2
import re
import sys
from threading import Thread
import time
from typing import List

def split_up_seeds_line(lines: List[str], number_of_seed_pairs: int = 1) -> List[List[str]]:
    lines_packs = []
    seed_pair_pattern = (r'\s').join([r'\d+\s\d+' for _ in range(number_of_seed_pairs)])
    matches = re.findall(seed_pair_pattern, lines[0])
    for match in matches:
        start_number, amount_to_add = [int(n) for n in match.split(' ')]
        new_seeds_line = f'seeds: {start_number} {amount_to_add}'
        lines_pack = [new_seeds_line] + lines[1:]
        lines_packs.append(lines_pack)
    
    return lines_packs


if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    start = time.time()
    line_packs = split_up_seeds_line(lines)
    
    lowest_locations = [None] * len(line_packs)
    threads: List[Thread] = []
    for index, line_pack in enumerate(line_packs):
        thread = Thread(target=pt2, args=[line_pack, lowest_locations, index])
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()
    
    print(f'Part 2 (multithreaded): {min(lowest_locations)}')     
    end = time.time()
    print(f'Part 2 (multithreaded) took {end - start}')