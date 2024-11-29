import sys
from math import floor

def solution(input_text):
    grid_heights = input_text.split('\n')
    gird_shortest_paths_lengths = ['.' * 5 for _ range(gri)]


    # function to return list of possible moves from an inputed square
    # for each square what is the shortest route 





if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    