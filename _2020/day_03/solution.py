"""
Solution to day 03
"""
from dataclasses import dataclass
from math import prod
from typing import List

TREE = '#'

@dataclass
class Coordinate:
    x: int
    y: int

def solution_part_01(input: str) -> str:
    map = [line.strip() for line in input.split('\n') if line]
    
    right_distance = 3
    down_distance = 1
    current_position = Coordinate(0,0)
    trees_seen = 0
    while is_on_map(current_position, map):
        if is_on_tree(current_position, map):
            trees_seen += 1
        current_position = move_coordinate(current_position, right_distance, down_distance, map)

    return str(trees_seen)

def is_on_map(coord: Coordinate, map: List[str]) -> bool:
    return coord.y < len(map)

def is_on_tree(coord: Coordinate, map: List[str]) -> bool:
    return map[coord.y][coord.x] == TREE

def move_coordinate(coord: Coordinate, right_distance: int, down_distance: int, map: List[str]) -> Coordinate:
    new_x = (coord.x + right_distance) % len(map[0])
    new_y = coord.y + down_distance
    new_coord = Coordinate(new_x, new_y)
    return new_coord

@dataclass
class Slope:
    x: int
    y: int

def solution_part_02(input: str) -> str:
    map = [line.strip() for line in input.split('\n') if line]
    
    slopes = [
        Slope(1, 1),
        Slope(3, 1),
        Slope(5, 1),
        Slope(7, 1),
        Slope(1, 2),
    ]
    trees_seen_for_slopes = []
    for slope in slopes:
        current_position = Coordinate(0,0)
        trees_seen = 0
        while is_on_map(current_position, map):
            if is_on_tree(current_position, map):
                trees_seen += 1
            current_position = move_coordinate(current_position, slope.x, slope.y, map)
        trees_seen_for_slopes.append(trees_seen)

    return str(prod(trees_seen_for_slopes))