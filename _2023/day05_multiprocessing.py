from day05_multithread import split_up_seeds_line
from day05 import pt2
import sys
from multiprocessing import Pool
import time

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')
    
    start = time.time()
    line_packs = split_up_seeds_line(lines)
    
    lowest_locations = [None] * len(line_packs)
    with Pool(5) as p:
        p.starmap(pt2, [(line_pack, lowest_locations, index) for index, line_pack in enumerate(line_packs)])
    
    print(f'Part 2 (multithreaded): {min(lowest_locations)}')     
    end = time.time()
    print(f'Part 2 (multithreaded) took {end - start}')