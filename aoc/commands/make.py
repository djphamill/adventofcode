import chevron

day = '' # TODO
year = '' # TODO

with open('/Users/david/adventofcode/aoc/commands/solution.mustache', 'r') as f:
    solution = chevron.render(f, {'mustache': 'World'})

with open(f'/Users/david/adventofcode/{year}/day_{day}/solution.py', 'w') as f:
    f.write(solution)