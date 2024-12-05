"""
Tests for day 05's solution
"""
from parameterized import parameterized
import pytest

from common.scenario import Scenario

from _2024.day_05.solution import solution_part_01, solution_part_02, Rule, Update, reorder
from _2024.day_05.tests.scenarios import part_01_scenarios, part_02_scenarios

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
    (Update(["3","4","5"]), 4),
    (Update(["5","78","92","1","2"]), 92),
])
def test_middle_page_of_update(update: Update, expected: int):
    actual = update.middle_page 
    assert actual == expected

@parameterized.expand([
    (Update([75,97,47,61,53]), Update([97,75,47,61,53])),
    (Update([61,13,29]), Update([61,29,13])),
    (Update([97,13,75,29,47]), Update([97,75,47,29,13]))
])
@pytest.mark.xfail
def test_reorder(update, expected):
    rules = [
        Rule(47,53),
        Rule(97,13),
        Rule(97,61),
        Rule(97,47),
        Rule(75,29),
        Rule(61,13),
        Rule(75,53),
        Rule(29,13),
        Rule(97,29),
        Rule(53,29),
        Rule(61,53),
        Rule(97,53),
        Rule(61,29),
        Rule(47,13),
        Rule(75,47),
        Rule(97,75),
        Rule(47,61),
        Rule(75,61),
        Rule(47,29),
        Rule(75,13),
        Rule(53,13),
    ]

    actual = reorder(update, rules)
    assert actual == expected