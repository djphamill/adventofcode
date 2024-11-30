"""
Make the files required for a given days/years solution
"""
from chevron import render

from aoc.commands.utils.paths import get_year_path, get_day_path, get_tests_path, get_templates_path, get_inputs_path, SOLUTION_TEMPLATE_FILE_NAME, SOLUTION_TEST_TEMPLATE_FILE_NAME, SCENARIOS_TEMPLATE_FILE_NAME, SOLUTION_FILE_NAME, TEST_FILE_NAME, SCENARIO_FILENAME, INPUT_FILENAME
from aoc.commands.utils.errors import DirAlreadyExists
from aoc.commands.utils.day import Day
from aoc.commands.utils.year import Year

def make(args):
    day: Day = args.day
    year: Year = args.year

    make_dirs(day, year)
    make_solution_file(day, year)
    make_solution_test_file(day, year)
    make_scenarios_file(day, year)
    make_input_files(day, year)


def make_dirs(day: Day, year: Year) -> None:
    year_path = get_year_path(year)
    if not year_path.exists():
        year_path.mkdir()

    day_path = get_day_path(day, year)
    if day_path.exists():
        raise DirAlreadyExists
    day_path.mkdir()

    tests_path = get_tests_path(day, year)
    tests_path.mkdir()

    inputs_path = get_inputs_path(day, year)
    inputs_path.mkdir()


def day_dir_already_exists(day: Day, year: Year):
    day_path = get_day_path(day, year)
    return day_path.exists()


def make_solution_file(day: Day, year: Year) -> None:
    solutions_template_path = get_templates_path(day, year) / SOLUTION_TEMPLATE_FILE_NAME
    with open(solutions_template_path, "r") as f:
        solution_code = render(f, {"day": day, "year": year})

    day_path = get_day_path(day, year)
    solution_path = day_path / SOLUTION_FILE_NAME

    with open(solution_path, "w") as f:
        f.write(solution_code)


def make_solution_test_file(day: Day, year: Year) -> None:
    solution_test_template_path = get_templates_path(day, year) / SOLUTION_TEST_TEMPLATE_FILE_NAME
    with open(solution_test_template_path, "r") as f:
        test_code = render(f, {"day": day, "year": year})

    tests_path = get_tests_path(day, year)
    solution_test_path = tests_path / TEST_FILE_NAME.format(day=day)

    with open(solution_test_path, "w") as f:
        f.write(test_code)

def make_scenarios_file(day: Day, year: Year) -> None:
    scenarios_template_path = get_templates_path(day, year) / SCENARIOS_TEMPLATE_FILE_NAME
    with open(scenarios_template_path, "r") as f:
        scenarios_code = render(f, {"day": day, "year": year})

    tests_path = get_tests_path(day, year)
    scenarios_path = tests_path / SCENARIO_FILENAME

    with open(scenarios_path, "w") as f:
        f.write(scenarios_code)

def make_input_files(day: Day, year: Year) -> None:
    _parts_in_a_day = 2
    _parts = list(range(1, _parts_in_a_day + 1))
    for part in _parts:
        input_file_path = get_inputs_path(day, year) / INPUT_FILENAME.format(part=part)
        input_file_path.touch()