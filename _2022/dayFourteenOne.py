import sys
from collections import namedtuple

Coord = namedtuple('Coordinate', ['x', 'y'])
INITIAL_POSITION = Coord(500, 0)
ROCK = '#'
AIR = '.'
SOURCE = '+'

def solution(input_text):
    # Build a 2-dimensional grid to represent the rock #, sand o and air .
    grid = build_grid(input_text)
    print_grid(grid)

    return ''
    abyss = the_abyss(grid)

    coord_of_sand = INITIAL_POSITION
    while not is_falling_into_the_abyss(coord_of_sand, abyss):
        coord_of_sand = INITIAL_POSITION

        while not is_at_rest(coord_of_sand, grid):
            coord_of_sand = move_sand(coord_of_sand, grid)
        
        grid = update_grid(coord_of_sand, grid)

    return

def build_grid(input_text):
    # A list of strings with the paths
    paths = input_text.split('\n')
    rows_of_vertices_as_string = [path.split(' -> ') for path in paths] 
    rows_of_vertices = []
    all_coords = []
    for row in rows_of_vertices_as_string:
        row_as_Coord = []
        for coord in row:
            x, y = coord.split(',')
            row_as_Coord.append(Coord(int(x), int(y)))
            all_coords.append(Coord(int(x), int(y)))
        rows_of_vertices.append(row_as_Coord)
    
    rock_points = []
    for row in rows_of_vertices:
        for i in range(len(row[1:])):
            start_vertex = row[i - 1]
            end_vertex = row[i]
            line = [start_vertex]

            if start_vertex.x != end_vertex.x:
                inbetween = range(1, start_vertex.x - end_vertex.x)
                for point in inbetween:
                    line.append(Coord(x=start_vertex.x + point, 
                                      y=start_vertex.y))
            else:
                inbetween = range(1, end_vertex.y - start_vertex.y)
                for point in inbetween:
                    line.append(Coord(x=start_vertex.x,
                                      y=start_vertex.y + point))
            
            line.append(end_vertex)

        rock_points.extend(line)
    
    smallest_x = min([coord.x for coord in all_coords])
    print(f'smallest x: {smallest_x}')
    largest_x = max([coord.x for coord in all_coords])
    print(f'largest x: {largest_x}')
    largest_y = max([coord.y for coord in all_coords])

    print(f'range x: {largest_x - smallest_x}')

    for i, point in enumerate(rock_points):
        rock_points[i] = Coord(x=point.x-smallest_x, y=point.y)

    top_row_of_grid = [AIR for _ in range(largest_x - smallest_x + 1)]
    top_row_of_grid[int(INITIAL_POSITION.x - smallest_x)] = SOURCE
    top_row_of_grid = ''.join(top_row_of_grid)

    print(top_row_of_grid)
    
    grid = [point + AIR * largest_y  for point in top_row_of_grid]
    for x, y in rock_points:
        grid[x] = grid[x][:y] + ROCK + grid[x][y+1:]
    print(grid)
    return grid

def print_grid(grid):
    """
    gird will be a list of strings, columns.
    """
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(f'{grid[j][i]}', end='')
        print('\n', end='')


def find_coords_of_rocks(rows_of_vertices):
    pass

def the_abyss(grid):
    # Return the position of the last # in a column
    return []


def write_output(grid):
    with open('output.txt', 'w') as f:
        for line in grid:
            f.write(line + '\n')

def is_falling_into_the_abyss(coord_of_sand):
    # Returns true if the sand is going to fall in to the abyss
    # and false if no
    return None

def is_at_rest(coord_of_sand):
    # Returns true if it cannot move and false if it can
    return None

def move_sand(coord_of_sand, grid):
    # Returns the next position of the sand
    return [0,0]

def update_grid(coord_of_sand, grid):
    # Returns the grid with th eposition of the restful sand included
    return [[],[]]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    