"""
Paths used in aoc program
    _year
    |-- day_01
    |   |-- solution.py
    |   |-- inputs
    |   |   |-- part_1.txt
    |   |   |-- part_2.txt
    |   |-- tests
    |       |-- scenarios.py
    |       |-- solution_test.py
    |-- day_02
    |   |-- solution.py
    |   |-- inputs
    |   |   |-- part_1.txt
    |   |   |-- part_2.txt
    |   |-- tests
    |       |-- scenarios.py
    |       |-- solution_test.py
"""
import os
import re
from pathlib import Path

from aoc.commands.utils.day import Day
from aoc.commands.utils.year import Year

class Filename(str):
    "Defines a filename"

    @property
    def extension(self) -> str:
        return self.split('.')[-1]
    
    @extension.setter
    def extension(self):
        raise "Cannot set this property"


SOLUTION_TEMPLATE_FILE_NAME = Filename('solution.mustache')
SOLUTION_TEST_TEMPLATE_FILE_NAME = Filename('test.mustache')
SCENARIOS_TEMPLATE_FILE_NAME = Filename('scenarios.mustache')

SOLUTION_FILE_NAME = Filename('solution.py')
TEST_FILE_NAME = Filename('day_{day}_solution_test.py')
SCENARIO_FILENAME = Filename('scenarios.py')
INPUT_FILENAME = Filename("part_{part}.txt")


def get_project_path() -> Path:
    utils_path, _ = os.path.split(__file__)
    project_path_pattern = r".*/adventofcode"
    match = re.match(project_path_pattern, utils_path)
    project_path = match.group(0)
    return Path(project_path)

def get_year_path(year: Year, relative: bool = False) -> Path:
    if relative:
        return Path(f'_{year}')
    else:
        return get_project_path() / f'_{year}'

def get_day_path(day: Day, year: Year, relative: bool = False) -> Path:
    year_path = get_year_path(year, relative)
    day_path = year_path / f'day_{day}'
    return day_path

def get_tests_path(day: Day, year: Year, relative: bool = False) -> Path:
    day_path = get_day_path(day, year, relative)
    tests_path = day_path / 'tests'
    return tests_path

def get_templates_path(day: Day, year: Year) -> Path:
    return get_project_path() / "aoc" / "templates"

def get_inputs_path(day: Day, year: Year) -> Path:
    return get_day_path(day, year) / 'inputs'