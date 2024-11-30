import sys

CYCLE_LENGTHS = {
    'noop' : 1,
    'addx' : 2
}

RECORD_VALUES_AT_CYCLES = [(i*40+20) for i in range(6)]

def solution(input_text):
    print(f'Recording values of register at cycle {RECORD_VALUES_AT_CYCLES}')

    commands = input_text.split('\n')
    current_cycle = 1
    register_value = 1
    total = 0

    for command in commands:
        if current_cycle in RECORD_VALUES_AT_CYCLES:
            print(f'A: total = {total} + {current_cycle} * {register_value}')
            total += current_cycle * register_value

        operation, value = command.split(' ') if len(command.split(' ')) == 2 else [command, None]
        # print(f'{operation}')

        if operation == 'addx':
            if current_cycle + 1 in RECORD_VALUES_AT_CYCLES:
                print(f'B: total = {total} + {current_cycle + 1} * {register_value}')
                total += (current_cycle + 1) * register_value
            register_value += int(value)
            current_cycle += 2
        else: 
            current_cycle += 1

    return total




if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    