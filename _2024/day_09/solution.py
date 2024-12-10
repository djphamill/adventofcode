"""
Solution to day 09
"""
from typing import List

def solution_part_01(input: str) -> str:
    disk_map = [int(char) for char in input]

    disk_space_required = calculate_disk_space_requried(disk_map)

    disk: List[int] = []

    forward_index = 0
    backward_index = -1
    while len(disk) < disk_space_required:
        fill_from_front = forward_index % 2 == 0
        if fill_from_front:
            block = [int(forward_index / 2) for _ in range(disk_map[forward_index])]
            for part in block:
                disk.append(part)
        else:
            block_size = disk_map[forward_index]
            block = []
            while len(block) < block_size:
                if disk_map[backward_index]:
                    block.append(int((len(disk_map) + backward_index) / 2))
                    new_disk_map_value =  disk_map[backward_index] - 1
                    disk_map[backward_index] = new_disk_map_value
                else:
                    backward_index -= 2 
            disk.extend(block)
        forward_index +=1
        
    checksum = sum([value * index for index, value in enumerate(disk)])
    return str(checksum)

def calculate_disk_space_requried(disk_map: List[int]) -> int:
    blocks_sizes = disk_map[::2]
    return sum(blocks_sizes)

def solution_part_02(input: str) -> str:
    pass