"""
Tests for day 04's solution
"""
from parameterized import parameterized

from common.scenario import Scenario

from _2024.day_04.solution import solution_part_01, solution_part_02, Gradient, Coordinate, makes_xmas, find_diagonally_adjacent_as
from _2024.day_04.tests.scenarios import part_01_scenarios, part_02_scenarios

@parameterized.expand(part_01_scenarios)
def test_solution_part_01(scenario: Scenario) -> str:
    expected = scenario.output
    actual = solution_part_01(scenario.input)
    assert actual == expected

def test_makes_xmas():
    map = ["MMMSXXMASM"
           "MSAMXMSMSA",
           "AMXSXMAAMM",
           "MSAMASMSMX",
           "XMASAMXAMM",
           "XXAMMXXAMA",
           "SMSMSASXSS",
           "SAXAMASAAA",
           "MAMMMXMMMM",
           "MXMXAXMASX"]
    
    x = Coordinate(5,0)
    gradient = Gradient(1,0)

    assert makes_xmas(x, map, gradient)

@parameterized.expand(part_02_scenarios)
def test_solution_part_02(scenario: Scenario) -> str:
    expected = scenario.output
    actual = solution_part_02(scenario.input)
    assert actual == expected

def test_find_diagonally_adjacent_as():
    map = [".M.S......",
           "..A..MSMS.",
           ".M.S.MAA..",
           "..A.ASMSM.",
           ".M.S.M....",
           "..........",
           "S.S.S.S.S.",
           ".A.A.A.A..",
           "M.M.M.M.M.",
           ".........."]
    m = Coordinate(7, 1)
    other_m = Coordinate(5, 1)

    expected = [Coordinate(6, 2)]
    actual = find_diagonally_adjacent_as(m, other_m, map) 
    assert actual == expected