"""
Make the files required for a given days/years solution
"""
import chevron
from datetime import datetime

this_year = datetime.now().strftime('%Y')

def make(args):
    day, year = args.day, args.year

    with open('/Users/david/adventofcode/aoc/commands/solution.py.mustache', 'r') as f:
        solution_code = chevron.render(f, {'day': day, 'year': year})

    print(f'solution.py:\n{solution_code}')
    # with open(f'/Users/david/adventofcode/{year}/day_{day}/solution.py', 'w') as f:
    #     f.write(solution_code)
