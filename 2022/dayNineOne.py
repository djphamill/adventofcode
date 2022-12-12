import sys
from copy import copy

HORIZONTAL = ['L', 'R']
VERTICAL = ['U', 'D']

def solution(input_text):
    moves =  input_text.split('\n')

    visited = [[0,0]] # list of comma-separated coordinates
    positions = {
        'H': [0, 0],
        'T': [0, 0]
    }

    moves = build_as_single_moves(moves)
    for move in moves:
        positions = make_move(move, positions)
        if positions['T'] not in visited:
            visited.append(copy(positions['T']))

    return len(visited)

def make_move(move, positions):
    
    if is_ontop(positions):
        # only change H
        positions = change_position(positions, move, 'H')
        return positions

    adjacent, alignment = adjacency_and_alignment(positions)
    if adjacent:
        if (alignment in HORIZONTAL and move in VERTICAL) or (alignment in VERTICAL and move in HORIZONTAL): 
            # 90-deg to tail --> move H, don't move T
            return change_position(positions, move, 'H')
        elif alignment == move: 
            # away from tail ---> move H, move T to H
            for end in 'H', 'T':
                positions = change_position(positions, move, end)
            return positions
        else: # over tail --> move H to T, don't move T
            return change_position(positions, move, 'H')
    
    # must be diagonal
    positions = change_position(positions, move, 'H')
    adjacent, alignment = adjacency_and_alignment(positions)
    if not adjacent:
        positions = change_position(positions, alignment[0], 'T')
        positions = change_position(positions, alignment[-1], 'T')
    
    return positions

def change_position(positions, direction, h_or_t):
    if direction == 'U':
        positions[h_or_t][1] += 1
    elif direction == 'D':
        positions[h_or_t][1] -= 1
    elif direction == 'R':
        positions[h_or_t][0] += 1
    elif direction == 'L':
        positions[h_or_t][0] -= 1
    
    return positions

def build_as_single_moves(moves):
    single_moves = []

    for move in moves:
        direction = move.split(' ')[0]
        repeats = int(move.split(' ')[1])
        for _ in range(repeats):
            single_moves.append(direction)

    return single_moves

def adjacency_and_alignment(positions):
    # Already handled 'on-top'
    head = positions['H']
    tail = positions['T']

    if is_ontop(positions):
        return False, 'ONTOP'

    for index, coordinate in enumerate(head):
        if tail[index] == coordinate:
            if index == 0:
                return True, 'D' if tail[1] > head[1] else 'U'
            else:
                return True, 'L' if tail[0] > head[0] else 'R'

    alignment = ''

    horizonatl_diff = head[0] - tail[0]
    vertical_diff = head[1] - tail[1]
    horizontal_letter = 'L' if horizonatl_diff < 0 else 'R'
    vertical_letter = 'D' if vertical_diff < 0 else 'U'

    for _ in range(abs(horizonatl_diff)):
        alignment += horizontal_letter
    for _ in range(abs(vertical_diff)):
        alignment += vertical_letter

    return False, alignment

def is_ontop(positions):
    return True if positions['H'] == positions['T'] else False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    