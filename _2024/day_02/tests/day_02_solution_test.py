"""
Tests for day 02's solution
"""
from parameterized import parameterized
import pytest

from common.scenario import Scenario

from _2024.day_02.solution import solution_part_01, solution_part_02
from _2024.day_02.tests.scenarios import part_01_scenarios, part_02_scenarios

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
