"""
Test path functions
"""
from pathlib import Path
from parameterized import parameterized

from aoc.commands.utils.paths import get_project_path, get_year_path, get_day_path
from aoc.commands.utils.day import Day
from aoc.commands.utils.year import Year

def test_get_project_path():
    expected = Path('/Users/david/adventofcode') # TODO: There is a better way of doing this?
    actual = get_project_path()

    assert actual == expected

@parameterized.expand([
    (Year(2024), False, Path('/Users/david/adventofcode/_2024')),
    (Year(2024), True, Path('_2024')),
])
def test_get_year_path(year, relative, expected):
    actual = get_year_path(year, relative)
    assert actual == expected

@parameterized.expand([
    (Day(19), Year(2024), False, Path('/Users/david/adventofcode/_2024/day_19')),
    (Day(19), Year(2024), True, Path('_2024/day_19')),
])
def test_get_day_path(day, year, relative, expected):
    actual = get_day_path(day, year, relative)
    assert actual == expected