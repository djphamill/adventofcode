"""
Tests for day 06's solution
"""
from parameterized import parameterized
import pytest

from common.scenario import Scenario

from _2024.day_06.solution import solution_part_01, solution_part_02, is_next_step_blocked, Position, Direction, move_guard
from _2024.day_06.tests.scenarios import part_01_scenarios, part_02_scenarios

@parameterized.expand(part_01_scenarios)
def test_solution_part_01(scenario: Scenario) -> str:
    expected = scenario.output
    actual = solution_part_01(scenario.input)
    assert actual == expected

@parameterized.expand(part_02_scenarios)
@pytest.mark.xfail
def test_solution_part_02(scenario: Scenario) -> str:
    expected = scenario.output
    actual = solution_part_02(scenario.input)
    assert actual == expected


@parameterized.expand([
    (Position(4, 1, Direction.UP.value), True),
    (Position(4, 1, Direction.RIGHT.value), False),
    (Position(9, 2, Direction.RIGHT.value), False),
    (Position(9, 0, Direction.DOWN.value), True),
])
def test_is_guard_blocked(guards_position, expected):
    map = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#..^.....",
        "........#.",
        "#.........",
        "......#...",
    ]
    actual = is_next_step_blocked(map, guards_position)
    assert actual  == expected

@parameterized.expand([
    (Position(4, 1, Direction.UP.value), Position(5, 1, Direction.RIGHT.value)),
    (Position(4, 1, Direction.RIGHT.value), Position(5, 1, Direction.RIGHT.value)),
    (Position(3, 0, Direction.RIGHT.value), Position(3, 1, Direction.DOWN.value)),
    (Position(9, 2, Direction.RIGHT.value), Position(10, 2, Direction.RIGHT.value)),
    (Position(9, 0, Direction.DOWN.value), Position(8, 0, Direction.LEFT.value)),
])
def test_move_guard(guards_position, expected):
    map = [
        "....#.....",
        ".........#",
        "..........",
        "..#.......",
        ".......#..",
        "..........",
        ".#........",
        "........#.",
        "#.........",
        "......#...",
    ]
    actual = move_guard(map, guards_position)
    assert actual  == expected