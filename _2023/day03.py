import re
import sys
from typing import List, Union, Tuple
from math import prod
from dataclasses import dataclass

@dataclass
class Point:
    row: int
    col: int

@dataclass
class Number:
    value: int
    row : int 
    start_col : int
    end_col: int

    @property
    def points(self) -> List[Point]:
        return [Point(self.row, col) for col in range(self.start_col, self.end_col + 1)]

@dataclass
class Star:
    row : int
    col : int

@dataclass
class Gear:
    star: Star
    adjacent_numbers: List[Number]
    
    @property
    def ratio(self): 
        return prod([number.value for number in self.adjacent_numbers])


def find_numbers(rows: List[str]) -> List[Number]:
    number_pattern = r'[0-9]+'
    numbers = []
    for row_number, row in enumerate(rows):
        matches = re.finditer(number_pattern, row)
        for match_ in matches:
            number = Number(int(match_[0]), row_number, match_.start(), match_.end() - 1)
            numbers.append(number)

    return numbers

def find_stars(rows: List[str]) -> List[Star]:
    star_pattern = r'\*'
    stars = []
    for row_number, row in enumerate(rows):
        matches = re.finditer(star_pattern, row)
        for match_ in matches:
            star = Star(row_number, match_.start())
            stars.append(star)

    return stars

def is_part_number(number: Number, rows: List[str]):
    start_row_index = number.row - 1 if number.row > 0 else 0
    end_row_index = number.row + 2 if number.row < len(rows) - 1 else len(rows)
    for row in rows[start_row_index: end_row_index]:
        start_col_index = number.start_col - 1 if number.start_col > 0 else 0
        end_col_index = number.end_col + 2 if number.end_col < len(row) - 1 else len(row)
        for char in row[start_col_index: end_col_index]:
            if char not in '.0123456789':
                return True
    return False

def convert_star_to_gear(star: Star, numbers: List[Number]) -> Union[Gear, None]:
    start_row_index = star.row - 1
    end_row_index = star.row + 1

    start_col_index = star.col - 1
    end_col_index = star.col + 1
    
    adjacent_numbers = []
    for number in numbers:
        for point in number.points:
            if number in adjacent_numbers:
                continue
            if start_col_index <= point.col <= end_col_index \
                    and start_row_index <= point.row <= end_row_index:
                adjacent_numbers.append(number)

    if len(adjacent_numbers) != 2:
        return None
    return Gear(star, adjacent_numbers)

def pt1(rows):
    part_numbers = []
    numbers = find_numbers(rows)
    for number in numbers:
        if is_part_number(number, rows):
            part_numbers.append(number.value)
    return sum(part_numbers)

def pt2(rows):
    gears = []
    numbers = find_numbers(rows)
    stars = find_stars(rows)
    for star in stars:
        gear = convert_star_to_gear(star, numbers)
        if gear:
            gears.append(gear)
    
    return sum([gear.ratio for gear in gears])


if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        rows = file.read().strip().split('\n')
    print(f'Part 1: {pt1(rows)}')
    print(f'Part 2: {pt2(rows)}')