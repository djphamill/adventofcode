import sys
from ast import literal_eval

def solution(input_text):
    lines = input_text.split('\n')
    number_of_pairs = int((len(lines) + 1) / 3)
    pairs_as_strings = [lines[i * 3:i * 3 + 2] for i in range(number_of_pairs)]
    
    pairs = read_string_as_list(pairs_as_strings)

    print_the_lists()

    return ''


def read_string_as_list(strings):



if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    