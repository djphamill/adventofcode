import sys
from dayEightOne import build_tree_rows_and_cols

def solution(input_text):
    
    tree_rows, tree_cols = build_tree_rows_and_cols(input_text)

    row_length = len(tree_rows[0])
    col_length = len(tree_cols[0])

    highest_scenic_score = 0

    for i in range(row_length):
        for j in range(col_length):
            current_sceninc_score = 1
            current_tree_height = tree_rows[i][j]
            views = build_views(tree_rows, tree_cols, i, j)
            for view in views:
                current_sceninc_score = current_sceninc_score * scenic_score(view, current_tree_height)
            
            if current_sceninc_score > highest_scenic_score:
                highest_scenic_score = current_sceninc_score

    return highest_scenic_score

def build_views(tree_rows, tree_cols, i, j):
    left = tree_rows[i][:j][::-1] # reverse
    right = tree_rows[i][j+1:]
    up = tree_cols[j][:i][::-1] # reverse
    down = tree_cols[j][i+1:]
    return [left, right, up, down]

def scenic_score(view, current_tree_height):
    count = 0 
    for tree_height in view:
        if tree_height < current_tree_height:
            count += 1
        else:
            count += 1
            return count

    return count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    