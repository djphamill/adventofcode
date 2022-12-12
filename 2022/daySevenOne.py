import sys
from re import match
from copy import copy

def solution(input_text):
    commands = input_text.split('\n')
    
    # success, line = confirm_no_cd_without_ls(commands)
    
    # if not success:
    #     sys.exit(f'No "$ ls" after moving in to a directory on line {line - 1}')

    files = build_files_dict(commands)

    folder_sizes = {}

    for file_path, file_size in files.items():
        file_path = file_path.split('/')[:-1]
        print(file_path)
        for folder in file_path:
            if folder not in folder_sizes:
                folder_sizes[folder] = file_size
            else:
                folder_sizes[folder] += file_size
    
    total = 0
    for size in folder_sizes.values():
        if size <= 100000:
            total += size

    return total

def confirm_no_cd_without_ls(commands):
    justMovedInToDir = False 

    for line, command in enumerate(commands):
        if justMovedInToDir and command != '$ ls':
            return False, line - 1

        if match('\$ cd [a-x,A-X]', command):
            justMovedInToDir = True
        else:
            justMovedInToDir = False

    return True, -1

def build_files_dict(commands):
    files = {}
    current_path = ['home']
    for command in commands:
        if match('\$ cd \.\.', command):
            current_path.pop()
        elif match('\$ cd \/', command):
            current_path = ['home']
        elif match('\$ cd [a-z,A-Z]', command):
            dir_name = command.split(' ')[-1]
            current_path.append(dir_name)
        elif match('[0-9]', command):
            file_name = command.split(' ')[-1]
            file_size = command.split(' ')[0]
            file_path = '/'.join(copy(current_path))
            if current_path:
               file_path += '/' 
            file_path += file_name
            files[file_path] = int(file_size)

    return files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    