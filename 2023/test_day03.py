from day03 import *
from parameterized import parameterized

@parameterized.expand([
    (Number(154, 1, 1, 3), ['.......',
                            '.154...',
                            '.......',
                            '..*....'], False),
    (Number(154, 1, 1, 3), ['...?...',
                            '.154...',
                            '.......',
                            '..*....'], True),
    (Number(23, 0, 1, 2), ['.23....',
                           '.1.....',
                           '.......',
                           '..*....'], False),
    (Number(23, 0, 1, 2), ['.23....',
                           '...!...',
                           '.......',
                           '..*....'], True),
    (Number(3, 3, 2, 2), ['.23....',
                          '...!...',
                          '.......',
                          '..3....'], False),
    (Number(3, 3, 2, 2), ['.23....',
                          '...!...',
                          '.......',
                          '..3....'
                          '.#.....'], False),
    (Number(3, 3, 2, 2), ['.23....',
                          '...!...',
                          '...?...',
                          '..3....'], True),
    (Number(3, 3, 2, 2), ['.23....',
                          '.......',
                          '.!.....',
                          '..3....'], True),
    (Number(23, 1, 1, 2), ['.23....',
                           '.23....',
                           '\......',
                           '.!.....',
                           '..3....'], True),
    (Number(23, 1, 1, 2), ['.23....',
                           '.23....',
                           '....\..',
                           '.!.....',
                           '..3....'], False),
    (Number(23, 1, 2, 3), ['!.23....',
                           '..23....',
                           '/....\..',
                           '..!.....',
                           '...3....'], False),
    (Number(923, 1, 2, 3), ['...!....',
                            '.923....',
                            '..23....',
                            '/....\..',
                            '..!.....',
                            '...3....'], True),
    (Number(923, 1, 1, 3), ['...%.',
                            '.923.',
                            '.....'], True),
])
def test_is_part_number(number, rows, expected):
    actual = is_part_number(number, rows)
    assert actual == expected


EXAMPLE = ["467..114..",
           "...*......",
           "..35..633.",
           "......#...",
           "617*......",
           ".....+.58.",
           "..592.....",
           "......755.",
           "...$.*....",
           ".664.598.."]

def test_find_numbers_one_row():
    rows = EXAMPLE[:1]
    expected = [Number(467, 0, 0, 2),
                Number(114, 0, 5, 7)]
    actual = find_numbers(rows)
    assert actual == expected

def test_find_numbers_three_rows():
    rows = ['.' for _ in range(7) ] + EXAMPLE[-3:]
    expected = [Number(755, 7, 6, 8),
                Number(664, 9, 1, 3),
                Number(598, 9, 5, 7)]
    actual = find_numbers(rows)
    assert actual == expected

def test_example_pt1():
    actual = pt1(EXAMPLE)
    expected = 4361
    assert actual == expected

def test_script_with_test_file():
    file_path = 'inputs/day03_example.txt'
    with open(file_path, 'r') as file:
        rows = file.read().strip().split('\n')

    actual = pt1(rows)
    expected = 4361
    assert actual == expected

@parameterized.expand([
    (Star(1, 3), Gear(Star(1, 3), [Number(467, 0, 0, 2),
                                   Number(35, 2, 2, 3)])),
    (Star(4, 3), None),
    (Star(8, 6), Gear(Star(8, 6), [Number(755, 7, 6, 8),
                                   Number(598, 9, 5, 7)]))
])
def test_convert_star_to_gear(star, expected):
    numbers = find_numbers(EXAMPLE)
    actual = convert_star_to_gear(star, numbers)
    assert actual == expected

def test_find_stars():
    expected = [Star(1, 3),
                Star(4, 3),
                Star(8, 5)]
    actual = find_stars(EXAMPLE)
    assert actual == expected

def test_example_pt2():
    file_path = 'inputs/day03_example.txt'
    with open(file_path, 'r') as file:
        rows = file.read().strip().split('\n')

    actual = pt2(rows)
    expected = 467835
    assert actual == expected