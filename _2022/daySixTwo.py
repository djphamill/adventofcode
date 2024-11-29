import sys

def solution(input_text):
    for index in range(13, len(input_text)):
        fourChars = input_text[index - 13:index + 1]
        if len(set(fourChars)) == len(fourChars):
            return index + 1 #Answers not 0 indexed

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some input text.')
    
    print(f'Solution is: {solution(sys.argv[1])}')



    