import sys

def solution(input_text):
    
    tree_rows, tree_cols = build_tree_rows_and_cols(input_text)

    row_length = len(tree_rows[0])
    col_length = len(tree_cols[0])

    visible_tree_count = 0

    for i in range(row_length):
        for j in range(col_length):
            if is_tree_visible(tree_rows, tree_cols, i, j):
                visible_tree_count += 1
    
    return visible_tree_count


def build_tree_rows_and_cols(input_text):
    tree_rows = input_text.split('\n')
    
    tree_cols = []
    for col_number in range(len(tree_rows[0])):
        col = ''
        for row in tree_rows:
            col += row[col_number]
        tree_cols.append(col)

    return tree_rows, tree_cols

def is_tree_visible(tree_rows, tree_cols, i, j):
    # make left, right, up, down lists
    current_tree_height = tree_rows[i][j]
    left = tree_rows[i][:j]
    right = tree_rows[i][j+1:][::-1] # reverse
    up = tree_cols[j][:i]
    down = tree_cols[j][i+1:][::-1] # reverse

    # if tree is max of one, return True
    for tree_heights in [left, right, up, down]:
        if len(tree_heights) == 0 : # Edge/corner
            return True 
        if current_tree_height > max(tree_heights):
            return True
    
    return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit('Provide some an input file.')
    
    input_file_path = sys.argv[1]

    with open(input_file_path, 'r') as f:
        input_text = f.read()

    print(f'Solution is: {solution(input_text)}')



    