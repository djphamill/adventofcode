import sys

CYCLE_LENGTHS = {
    'noop' : 1,
    'addx' : 2
}

PIXEL = {
    'on': '#',
    'off': '.'
}

def solution(input_text):
    commands = iter(input_text.split('\n'))
    current_cycle = 1 # Not zero indexed
    sprite_position = sprite_position_list(1) # Zero indexed
    pixels = ['' for _ in range(240)] # Zero indexed 
    in_mid_operation = False

    for current_cycle in range(1, 241):
        if (current_cycle % 40) - 1 in sprite_position:
            pixels[current_cycle - 1] = PIXEL['on']
        else:
            pixels[current_cycle - 1] = PIXEL['off'] 
        
        if in_mid_operation:
            in_mid_operation = False
            sprite_position = sprite_position_list(sprite_position[1] + int(value))
            continue
        else:
            command = next(commands)
            
        operation, value = command.split(' ') if len(command.split(' ')) == 2 else [command, None]

        if operation == 'addx':
            in_mid_operation = True

    rows = [''.join(pixels[(i-1)*40:i*40]) for i in range(1, 7)]
    screen = '\n'.join(rows)
    
    return screen

def sprite_position_list(middle):
    return [i for i in range(middle - 1, middle +2)]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is:\n{solution(input_text)}')



    