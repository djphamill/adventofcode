"""
Tests for day 07's solution
"""
from parameterized import parameterized

from common.scenario import Scenario

from _2024.day_07.solution import solution_part_01, solution_part_02, concatenate
from _2024.day_07.tests.scenarios import part_01_scenarios, part_02_scenarios

@parameterized.expand(part_01_scenarios)
def test_solution_part_01(scenario: Scenario) -> str:
    expected = scenario.output
    actual = solution_part_01(scenario.input)
    assert actual == expected

@parameterized.expand(part_02_scenarios)
def test_solution_part_02(scenario: Scenario) -> str:
    expected = scenario.output
    actual = solution_part_02(scenario.input)
    assert actual == expected

@parameterized.expand([
    (12, 13, 1213),
    (2, 3999, 23999),
])
def test_concatenate(first: int, second: int, expected: int):
    actual = concatenate(first, second)
    assert actual == expected