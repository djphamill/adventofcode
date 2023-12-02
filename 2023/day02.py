import sys
import re
from typing import List
from math import prod

game_id_pattern = r'(?<=Game )(\d*)(?=:)'

max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def pt1(games: List[str]) -> int:
    possible_games = []
    for game in games:
        game_id = re.search(game_id_pattern, game)
        game_possible = True
        for colour, max_number in max_cubes.items():
            if not game_possible:
                break
            matches = re.findall(rf'(?<=\s)\d*(?=\s{colour})', game)
            for match in matches:
                if int(match) > max_number:
                    game_possible = False

        if game_possible:    
            possible_games.append(int(game_id[0]))

    return sum(possible_games)

def pt2(games: List[str]) -> int:
    game_powers: List[int] = []
    for game in games:
        max_of_each_colour = []
        for colour in max_cubes:
            cube_counts = [int(match) for match in re.findall(rf'(?<=\s)\d*(?=\s{colour})', game)]
            max_of_each_colour.append(max(cube_counts))
        game_powers.append(prod(max_of_each_colour))
    return sum(game_powers)

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        games = file.read().split('\n')
    print(pt1(games))
    print(pt2(games))

