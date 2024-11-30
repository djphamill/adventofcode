def main():
    with open('dayFive-input.txt', 'r') as f:
        l = f.read().split('\n')

    stacks, moves = build_stacks_and_moves(l)

    for move in moves:
        stacks = stacks_after_move(stacks, move)
    
    return top_of_each_stack(stacks)
 

def build_stacks_and_moves(string_list):
    """
    Returns 
        stacks, a list of lists containing the crates in each stack - top most
            crate will be end element
        moves, a list of dicts (keys: number, from, to) - to be applied in order
    """

    # find the empty string element and slice list 
    #   (excluding empty list element and element before that, the stack number row)
    stacks_strings, moves_strings = split_into_stacks_moves_strings(string_list)

    # loop through stacks half
    #   grab every third element starting from 1 ( 0 * 3 + 1 ) up to 19 ( 8 * 3 + 1)
    #   check if empty string, if not prepend it to correct stack
    stacks = build_stacks_list(stacks_strings)

    moves = []
    for move in moves_strings:
        moves.append(build_move_dict(move))

    return stacks, moves


def split_into_stacks_moves_strings(string_list):
    """
    Return two lists, splitting the string_list at the empty row, removing that emtpy row and 
    the stack numbers row
    """
    empty_index = string_list.index('')
    stack_numbers_index = empty_index - 1 
    stacks_strings = string_list[:stack_numbers_index]
    moves_strings = string_list[empty_index + 1:]
    return stacks_strings, moves_strings


def build_move_dict(move_string):
    """
    Returns a move dict from a move as a string
    """
    move = move_string.split(' ')
    return {
        'number': int(move[1]),
        'from': int(move[3]),
        'to': int(move[5])
    }

def stacks_after_move(stacks, move):
    """
    Return stacks after the move has been applied
    """
    number_to_move = move['number']
    from_stack = move['from'] - 1 # to account for 0 indexing
    to_stack = move['to'] - 1 # to account for 0 indexing
    
    for _ in range(number_to_move):
        stacks[to_stack].append(stacks[from_stack].pop())

    return stacks


def top_of_each_stack(stacks):
    """
    Returns a string of the crates at the top of each stack
    """
    top_crates = ''

    for stack in stacks:
        top_crates += stack[-1]

    return top_crates

def build_stacks_list(stacks_strings):
    """
    Returns list of stacks, assuming no empty stack
    """
    number_of_stacks = int((len(stacks_strings[0]) + 1) / 4)
    print(f'number of stacks: {number_of_stacks}')
    stacks = [[] for _ in range(number_of_stacks)]
    for row in stacks_strings:
        for stack_number in range(number_of_stacks):
            print(stack_number)
            print(row)
            crate = row[stack_number * 4 + 1]
            print(crate)
            if crate.isalpha(): # incase haven't reach top of stack
                stacks[stack_number] = [crate] + stacks[stack_number]

    return stacks

if __name__ == "__main__":
    solution = main()
    print(f'The solutions is: {solution}')