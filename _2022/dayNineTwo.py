import sys
from copy import copy

HORIZONTAL = ['L', 'R']
VERTICAL = ['U', 'D']

def solution(input_text):
    moves =  input_text.split('\n')

    motions = {}

    moves = build_as_single_moves(moves)
    
    # loop through knots (1, 2, ..., 9)
    for tail_knot_number in range(1, 10):
        positions = {
                'H': [0,0],
                'T': [0,0]
            }

        motion_of_tail = [[0,0]]

        # loop through moves, return motion_of_tail
        for move in moves:
            positions = make_move(move, positions) 

            if positions['T'] != motion_of_tail[-1]:
                # print(f'{tail_knot_number}: Add to motion of tail, {positions["T"]}')
                motion_of_tail.append(copy(positions['T']))
                # print(f'............ is now {motion_of_tail}')

        # set new head and tail postions
        if tail_knot_number != 9:
            motions[tail_knot_number] = copy(motion_of_tail)
            moves = build_new_moves(copy(motion_of_tail))
        else:
            for knot, motion in motions.items():
                print(f'{knot}: {motions}')
            print(motion_of_tail)
            print(len(motion_of_tail))
            return len(set([str(coord) for coord in motion_of_tail]))


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
    if 'U' in direction:
        positions[h_or_t][1] += 1
    if 'D' in direction:
        positions[h_or_t][1] -= 1
    
    if 'R' in direction:
        positions[h_or_t][0] += 1
    if 'L' in direction:
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

def build_new_moves(motion_of_tail):
    moves = []
    for index, new_coord in enumerate(motion_of_tail[1:], 1):
        move = ''
        prev_coord = motion_of_tail[index - 1]
        if new_coord[0] > prev_coord[0]: # left
            move += 'R'
            moves.append(move)
            move = ''
        elif new_coord[0] < prev_coord[0]: # right
            move += 'L'
            moves.append(moves)
            move = ''

        if new_coord[1] > prev_coord[1]: # up
            move += 'U'
        elif new_coord[1] < prev_coord[1]: # down
            move += 'D'

        moves.append(move)
    
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    