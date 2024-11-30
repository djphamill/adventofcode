"""
Find the solution for that day/years AOC problem
Place input in to that solution
"""
from pathlib import Path
import importlib

from aoc.commands.utils.day import Day
from aoc.commands.utils.year import Year
from aoc.commands.utils.part import Part
from aoc.commands.utils.paths import get_inputs_path, INPUT_FILENAME

def solve(args):
    day: Day = args.day
    year: Year = args.year
    
    part: Part = args.part

    input_file_path = get_inputs_path(day, year) / INPUT_FILENAME.format(part=part)
    input = read_input(input_file_path)

    importlib.invalidate_caches()
    solution = importlib.import_module(f'_{year}.day_{day}.solution')
    if part == 1:
        output = solution.solution_part_01(input)
    elif part == 2:
        output = solution.solution_part_02(input)
    else:
        raise Exception('Something went wrong')
    print(output)

def read_input(input_file_path: Path) -> str:
    with open(input_file_path, "r") as f:
        input = f.read()
    return input