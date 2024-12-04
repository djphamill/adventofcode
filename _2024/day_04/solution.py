"""
Solution to day 04
"""
from dataclasses import dataclass
from typing import List

@dataclass
class Coordinate:
    right: int
    down: int

    def character_at(self, map: List[str]) -> str:
        return map[self.down][self.right]
    
    def on_same_row(self, other: 'Coordinate'):
        return self.down == other.down

@dataclass
class Gradient:
    right: int
    down: int

GRADIENTS_TO_SEARCH = [
    Gradient(-1,-1),
    Gradient(-1,0),
    Gradient(-1,1),
    Gradient(0,-1),
    Gradient(0,1),
    Gradient(1,-1),
    Gradient(1,0),
    Gradient(1,1),
]

XMAS = "XMAS"

def solution_part_01(input: str) -> str:
    map = [line.strip() for line in input.split('\n') if line]

    all_x = final_all(map, XMAS[0])
    word_count = 0
    for x in all_x:
        word_count_for_x = count_words_for_x(map, x)
        word_count += word_count_for_x
    
    return str(word_count)


def final_all(map: List[str], letter_to_find: str) -> List[Coordinate]:
    coordinates = []
    for down_distance, row in enumerate(map):
        for right_distance, char in enumerate(row):
            if char == letter_to_find:
                coordinates.append(Coordinate(right_distance, down_distance))

    return coordinates

def count_words_for_x(map: List[str], x: Coordinate) -> int:
    word_count_for_x = 0
    for gradient_to_search in GRADIENTS_TO_SEARCH:
        if makes_xmas(x, map, gradient_to_search):
            word_count_for_x += 1
    
    return word_count_for_x

def makes_xmas(x: Coordinate, map: List[str], gradient: Gradient) -> bool:
    coordinate_of_next_char = x
    for letter_needed in XMAS[1:]:
        coordinate_of_next_char = Coordinate(coordinate_of_next_char.right + gradient.right, coordinate_of_next_char.down + gradient.down)
        if is_outside_map(map, coordinate_of_next_char):
            return False
        next_char = coordinate_of_next_char.character_at(map)
        if next_char != letter_needed:
            return False
    return True
        
def is_outside_map(map: List[str], coordinate: Coordinate) -> bool:
    length_of_map = len(map[0])
    if coordinate.right >= length_of_map or coordinate.right < 0:
        return True

    height_of_map = len(map)
    if coordinate.down >= height_of_map or coordinate.down < 0:
        return True
    
    return False

MAS = "MAS"

def solution_part_02(input: str) -> str:
    map = [line.strip() for line in input.split('\n') if line]

    all_m = final_all(map, MAS[0])
    xmas_count = 0
    for m in all_m:
        xmas_count_for_m = count_x_mas(map, m)
        xmas_count += xmas_count_for_m
    
    return str(int(xmas_count / 2)) # Will double count x-mas

def count_x_mas(map: List[str], m: Coordinate) -> int:
    ms_in_corners = find_ms_in_corners(m, map)
    if not ms_in_corners:
        return 0
    
    xmas_count_for_m = 0
    for m_in_corner in ms_in_corners:
        diagonally_adjacent_as = find_diagonally_adjacent_as(m, m_in_corner, map)
        if not diagonally_adjacent_as:
            continue

        for a in diagonally_adjacent_as:
            if has_s(m, a, map) and has_s(m_in_corner, a, map):
                xmas_count_for_m +=1
    
    return xmas_count_for_m

GRADIENTS_TO_CORNERS = [
    Gradient(-2,0),
    Gradient(0,-2),
    Gradient(0,2),
    Gradient(2,0),
]
    
def find_ms_in_corners(m: Coordinate, map: List[str]) -> List[Coordinate]:
    ms_in_corners = []
    for gradient in GRADIENTS_TO_CORNERS:
        corner_coordinate = Coordinate(m.right + gradient.right, m.down + gradient.down)
        if is_outside_map(map, corner_coordinate):
            continue

        letter_in_corner = corner_coordinate.character_at(map)
        if letter_in_corner == MAS[0]:
            ms_in_corners.append(Coordinate(m.right + gradient.right, m.down + gradient.down))
    
    return ms_in_corners

def find_diagonally_adjacent_as(m: Coordinate, other_m: Coordinate, map: List[str]) -> List[Coordinate]:
    if m.on_same_row(other_m):
        diagonally_adjacent_as = find_as_for_same_row_ms(m, other_m, map)
    else:
        diagonally_adjacent_as = find_as_for_same_col_ms(m, other_m, map)
    return diagonally_adjacent_as

def find_as_for_same_col_ms(m: Coordinate, other_m: Coordinate, map: List[str]) -> List[Coordinate]:
    diagonally_adjacent_as = []

    midpoint = int((m.down + other_m.down) / 2)
    cooridinate_diagonally_left = Coordinate(m.right - 1, midpoint)
    is_diagonally_left_a = is_a(cooridinate_diagonally_left, map)
    if is_diagonally_left_a:
        diagonally_adjacent_as.append(cooridinate_diagonally_left)

    cooridinate_diagonally_right = Coordinate(m.right + 1, midpoint)
    is_diagonally_right_a = is_a(cooridinate_diagonally_right, map)
    if is_diagonally_right_a:
        diagonally_adjacent_as.append(cooridinate_diagonally_right)
    
    return diagonally_adjacent_as

def find_as_for_same_row_ms(m: Coordinate, other_m: Coordinate, map: List[str]) -> List[Coordinate]:
    diagonally_adjacent_as = []

    midpoint = int((m.right + other_m.right) / 2)
    cooridinate_diagonally_up = Coordinate(midpoint, m.down - 1)
    is_diagonally_up_a = is_a(cooridinate_diagonally_up, map)
    if is_diagonally_up_a:
        diagonally_adjacent_as.append(cooridinate_diagonally_up)

    cooridinate_diagonally_down = Coordinate(midpoint, m.down + 1)
    is_diagonally_down_a = is_a(cooridinate_diagonally_down, map)
    if is_diagonally_down_a:
        diagonally_adjacent_as.append(cooridinate_diagonally_down)
    
    return diagonally_adjacent_as

def is_a(coordinate: Coordinate, map: List[str]) -> bool:
    if is_outside_map(map, coordinate):
        return False
    char = coordinate.character_at(map)
    if char == MAS[1]:
        return True
    return False

def has_s(m: Coordinate, a: Coordinate, map: List[str]):
    change_in_right = a.right - m.right
    change_in_down = a.down - m.down
    gradient = Gradient(change_in_right, change_in_down)

    coordinate_of_letter = Coordinate(a.right + gradient.right, a.down + gradient.down)
    if is_outside_map(map, coordinate_of_letter):
        return False

    letter = coordinate_of_letter.character_at(map)
    if letter == MAS[2]:
        return True
    return False