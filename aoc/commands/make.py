import chevron
from datetime import datetime

this_year = datetime.now().strftime('%Y')

def make(day, year=this_year): # TODO: do this better
    day = '' # TODO
    year = '' # TODO

    with open('/Users/david/adventofcode/aoc/commands/solution.py.mustache', 'r') as f:
        solution = chevron.render(f, {'mustache': 'World'})

    print(f'solution.py: {solution}')

    # with open(f'/Users/david/adventofcode/{year}/day_{day}/solution.py', 'w') as f:
    #     f.write(solution)
