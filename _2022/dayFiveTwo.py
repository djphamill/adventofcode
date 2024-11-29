from .dayFiveOne import build_stacks_and_moves, top_of_each_stack

def main():
    with open('dayFive-input.txt', 'r') as f:
        l = f.read().split('\n')

    stacks, moves = build_stacks_and_moves(l)

    for move in moves:
        stacks = stacks_after_move_maintain_order(stacks, move)
    
    return top_of_each_stack(stacks)
 
def stacks_after_move_maintain_order(stacks, move):
    """
    Return stacks after the move has been applied
    """
    number_to_move = move['number']
    from_stack = move['from'] - 1 # to account for 0 indexing
    to_stack = move['to'] - 1 # to account for 0 indexing
    
    stacks[to_stack].extend(stacks[from_stack][-1 * number_to_move:])
    for _ in range(number_to_move):
        stacks[from_stack].pop()

    return stacks


if __name__ == "__main__":
    solution = main()
    print(f'The solutions is: {solution}')