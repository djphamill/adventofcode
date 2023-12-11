from dataclasses import dataclass
import sys
import time
from typing import List


class ConnectionResolver:
    
    @staticmethod
    def connected_to(tile: 'Tile') -> List[tuple[int]]:
        x, y = tile.x, tile.y
        shape = tile.shape
    
        north = (x, y - 1)
        east = (x + 1, y)
        south = (x, y + 1)
        west = (x - 1, y)
        
        match shape:
            case '|':
                return [north, south]
            case '-':
                return [east, west]
            case 'L':
                return [north, east]
            case 'J':
                return [north, west]
            case '7':
                return [south, west]
            case 'F':
                return [east, south]               
        
        return []

@dataclass
class Tile:
    shape: str
    x: int
    y: int
    
    @property
    def position(self) -> tuple[int]:
        return self.x, self.y
    
    @property
    def connected_to(self) -> List[tuple[int]]:
        return ConnectionResolver.connected_to(self)
    

def pt1(lines: List[str]) -> int:
    loop_tiles = find_loop_tiles(lines)
    steps = len(loop_tiles) - 1
    return int(steps / 2)

def find_starting_position(lines: List[str]) -> tuple[int]:
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == 'S':
                return x, y

def find_first_tiles(lines: List[str]) -> tuple[Tile]:
    start_x, start_y = find_starting_position(lines)
    start_tile = Tile('S', start_x, start_y)
    
    possible_first_tiles = []
    for dx in [-1, 0, +1]:
        for dy in [-1, 0, +1]:
            if dx + dy in [-2, 0, 2]:
                continue
            x = start_tile.x + dx
            y = start_tile.y + dy
            if x < 0 or y < 0 or x > len(lines[0]) or y > len(lines):
                continue
            shape = lines[y][x]
            tile = Tile(shape, x, y)
            if (start_tile.x, start_tile.y) in tile.connected_to:
                possible_first_tiles.append(tile)
                
    return start_tile, possible_first_tiles[0]


def pt2(lines: List[str]) -> int:
    loop_tiles = find_loop_tiles(lines)
    # Read each char from top left to bottom right. 
    # First non-loop edge tile is not in the loop.

def inflate_map(lines) -> List[str]:
    inflated_map = []
    for row in lines:
        new_row = ''
        for char in row[:-1]:
            new_row += char + '*'
        new_row += row[-1]
        inflated_map.append(new_row)
        inflated_map.append('*' * len(new_row))
    inflated_map.pop(-1)
    
    return inflated_map

def find_loop_tiles(lines: List[str]) -> List[Tile]:
    start_tile, first_tile = find_first_tiles(lines)
    
    loop_tiles = []
    previous_tile = start_tile
    current_tile = first_tile
    loop_tiles.extend([start_tile, first_tile])
    at_S = False
    while not at_S:
        possible_next_positions = current_tile.connected_to
        next_x, next_y = [p for p in possible_next_positions if p != (previous_tile.x, previous_tile.y)][0]
        previous_tile = current_tile
        next_shape = lines[next_y][next_x]
        current_tile = Tile(next_shape, next_x, next_y)
        loop_tiles.append(current_tile)
        if current_tile.shape == 'S':
            break
    return loop_tiles

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