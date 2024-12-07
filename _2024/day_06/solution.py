"""
Solution to day 06
"""
from dataclasses import dataclass
from typing import List, Set
from enum import Enum
from pairing import pair

class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

@dataclass
class Position:
    right: int
    down: int
    direction: Direction

    def is_coordinate_on_map(self, map: List[str]) -> bool:
        return self.right >= 0 and self.down >= 0 and self.right < len(map[0]) and self.down < len(map)

    def turn_right(self) -> 'Position':
        if self.direction == Direction.UP.value:
            new_direction = Direction.RIGHT.value
        elif self.direction == Direction.RIGHT.value:
            new_direction = Direction.DOWN.value
        elif self.direction == Direction.DOWN.value:
            new_direction = Direction.LEFT.value
        else:
            new_direction = Direction.UP.value
        
        return Position(self.right, self.down, new_direction)

    def step_forward(self) -> 'Position':
        if self.direction == Direction.UP.value:
            return Position(self.right, self.down - 1, self.direction)
        if self.direction == Direction.RIGHT.value:
            return Position(self.right + 1, self.down, self.direction)
        if self.direction == Direction.DOWN.value:
            return Position(self.right, self.down + 1, self.direction)
        if self.direction == Direction.LEFT.value:
            return Position(self.right - 1, self.down, self.direction)
        
    def __hash__(self) -> int:
        return pair(self.right, self.down, safe=True)

def solution_part_01(input: str) -> str:
    map = [line.strip() for line in input.split('\n') if line]
    
    guards_position = find_guard(map)
    guards_path: Set[Position] = set()

    while guards_position.is_coordinate_on_map(map):
        guards_path.add((guards_position.right, guards_position.down))
        guards_position = move_guard(map, guards_position)
    
    return str(len(guards_path))

def find_guard(map: List[str]) -> Position:
    for row_number, row in enumerate(map):
        for col_number, char in enumerate(row):
            if char == '^':
                return Position(col_number, row_number, Direction.UP.value)
    
def move_guard(map: List[str], guard_position: Position) -> Position:
    if is_next_step_blocked(map, guard_position):
        guard_position = guard_position.turn_right()
    guards_new_position = guard_position.step_forward()
    return guards_new_position

def is_next_step_blocked(map: List[str], guard_position: Position) -> bool:
    next_step = guard_position.step_forward()
    if not next_step.is_coordinate_on_map(map):
        return False
    character_at_next_step = map[next_step.down][next_step.right]
    return character_at_next_step == "#"

def solution_part_02(input: str) -> str:
    map = [line.strip() for line in input.split('\n') if line]
    
    guards_position = find_guard(map)
    guards_path: List[Position] = []

    while guards_position.is_coordinate_on_map(map):
        guards_path.append(guards_position)
        guards_position = move_guard(map, guards_position)
    
    places_for_blocks_that_create_loops = find_loop_making_blocks(guards_path, map)
    return str(len(places_for_blocks_that_create_loops))

@dataclass
class Coordinate:
    right: int
    down: int

def find_loop_making_blocks(path: List[Position], map: List[str]) -> List[Coordinate]:
    coordiantes_of_loop_making_blocks: List[Coordinate] = []
    for number_of_steps_taken, position in enumerate(path):
        path_to_check = path[:number_of_steps_taken]
        if path_contains_trail_to_right(position, path_to_check, map):
            coordinate_of_loop_making_block = calculate_position_of_loop_making_block(position)
            coordiantes_of_loop_making_blocks.append(coordinate_of_loop_making_block)
    return coordiantes_of_loop_making_blocks
    
def path_contains_trail_to_right(position: Position, path: List[Position], map: List[str]) -> bool:
    positions_to_find = get_positions_to_find(position, map)
    for position_to_find in positions_to_find:
        for path_point in path:
            if path_point == position_to_find:
                return True

    return False
    
def get_positions_to_find(position: Position, map: List[str]) -> List[Position]:
    height_of_map = len(map)
    width_of_map = len(map[0])
    
    positions: List[Position]= []
    if position.direction == Direction.UP.value:
        for right in range(position.right + 1, width_of_map):
           positions.append(Position(right, position.down, Direction.RIGHT.value))
    elif position.direction == Direction.RIGHT.value:
        for down in range(position.down + 1, height_of_map):
           positions.append(Position(position.right, down, Direction.DOWN.value))
    elif position.direction == Direction.DOWN.value:
        for right in range(position.right):
           positions.append(Position(right, position.down, Direction.LEFT.value))
    else:
        for down in range(position.down):
            positions.append(Position(position.right, down, Direction.UP.value))
    return positions


def calculate_position_of_loop_making_block(position: Position) -> Coordinate:
    one_step_forward = position.step_forward()
    return Coordinate(one_step_forward.right, one_step_forward.down)