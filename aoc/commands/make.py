"""
Make the files required for a given days/years solution
"""
import chevron

from aoc.commands.utils.constants import project_path

def make(args):
    day, year = args.day, args.year

    with open('/Users/david/adventofcode/aoc/templates/solution.mustache', 'r') as f:
        solution_code = chevron.render(f, {'day': day, 'year': year})

    with open('/Users/david/adventofcode/aoc/templates/test.mustache', 'r') as f:
        test_code = chevron.render(f, {'day': day, 'year': year})

    print(f'{project_path}/{year}/solution.py:\n{solution_code}')
    print(f'{project_path}/{year}/tests/day_{day}_test.py:\n{test_code}')
    # with open(f'/Users/david/adventofcode/{year}/day_{day}/solution.py', 'w') as f:
    #     f.write(solution_code)
