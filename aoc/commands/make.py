"""
Make the files required for a given days/years solution
"""
import chevron
from datetime import datetime

def make(args):
    day, year = args.day, args.year

    with open('/Users/david/adventofcode/aoc/templates/solution.mustache', 'r') as f:
        solution_code = chevron.render(f, {'day': day, 'year': year})

    with open('/Users/david/adventofcode/aoc/templates/test.mustache', 'r') as f:
        test_code = chevron.render(f, {'day': day, 'year': year})

    print(f'solution.py:\n{solution_code}')
    print(f'test.py:\n{test_code}')
    # with open(f'/Users/david/adventofcode/{year}/day_{day}/solution.py', 'w') as f:
    #     f.write(solution_code)
