"""
Tests for day 08's solution
"""
from parameterized import parameterized

from common.scenario import Scenario

from _2024.day_08.solution import solution_part_01, solution_part_02, find_internal_antinodes, Antenna, Antinode, find_external_antinodes
from _2024.day_08.tests.scenarios import part_01_scenarios, part_02_scenarios

@parameterized.expand(part_01_scenarios)
def test_solution_part_01(scenario: Scenario) -> str:
    expected = scenario.output
    actual = solution_part_01(scenario.input)
    assert actual == expected


def test_find_internal_antinodes_for_antennae_right_and_down():
    antennae = [Antenna(1, 1, "A"), Antenna(4, 7, "A")]
    expected = [Antinode(2, 3, antennae), Antinode(3, 5, antennae[::-1])]
    
    actual = find_internal_antinodes(antennae)
    assert actual == expected

def test_find_internal_antinodes_for_antennae_left_and_down():
    antennae = [Antenna(4, 1, "A"), Antenna(1, 7, "A")]
    expected = [Antinode(3, 3, antennae), Antinode(2, 5, antennae[::-1])]
    
    actual = find_internal_antinodes(antennae)
    assert actual == expected

def test_find_internal_antinodes_for_antennae_right_and_up():
    antennae = [Antenna(1, 7, "A"), Antenna(4, 1, "A")]
    expected = [Antinode(2, 5, antennae), Antinode(3, 3, antennae[::-1])]
    
    actual = find_internal_antinodes(antennae)
    assert actual == expected

@parameterized.expand(part_02_scenarios)
def test_solution_part_02(scenario: Scenario) -> str:
    expected = scenario.output
    actual = solution_part_02(scenario.input)
    assert actual == expected
