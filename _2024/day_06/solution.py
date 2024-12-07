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
    pass