import unittest
from ..dayEightOne import build_tree_rows_and_cols, is_tree_visible

class TestDay08(unittest.TestCase):
    """
    Test functions created for Day04 tasks
    """

    INPUT_FILE = '/Users/djph/Library/Mobile Documents/com~apple~CloudDocs/repos/adventofcode/2022/data/dayEight-input-test-01.txt'

    TREE_GRID = [[[4], [4], [3], [4], [4]],
                 [[5], [3], [7], [8], [4]],
                 [[9], [8], [7], [1], [4]],
                 [[4], [5], [6], [7], [8]]]

    def test_build_tree_rows_and_cols(self):
        """
        Test build_tree_rows_and_cols
        """
        with open(self.INPUT_FILE,'r') as f:
            input_text = f.read()

        rows, cols = build_tree_rows_and_cols(input_text)
        expectedRows = ['44344', '53784', '98714', '45678']
        expectedCols = ['4594', '4385', '3776', '4817', '4448']

        self.assertEqual(rows, expectedRows)
        self.assertEqual(cols, expectedCols)

    def test_is_tree_visible_inside(self):
        """
        Test is_tree_visible for interior tree
        """

        with open(self.INPUT_FILE,'r') as f:
            input_text = f.read()

        rows, cols = build_tree_rows_and_cols(input_text)

        row = 1
        col = 2

        visibility = is_tree_visible(rows, cols, row, col)
        expectedVisibility = True

        self.assertEqual(visibility, expectedVisibility)
    
    def test_is_tree_visible_edge(self):
        """
        Test is_tree_visible for edge
        """
        with open(self.INPUT_FILE,'r') as f:
            input_text = f.read()

        rows, cols = build_tree_rows_and_cols(input_text)

        row = 0
        col = 3

        visibility = is_tree_visible(rows, cols, row, col)
        expectedVisibility = True

        self.assertEqual(visibility, expectedVisibility)
    
    def test_is_tree_visible_corner(self):
        """
        Test is_tree_visible for edge
        """
        with open(self.INPUT_FILE,'r') as f:
            input_text = f.read()

        rows, cols = build_tree_rows_and_cols(input_text)

        row = 3
        col = 0

        visibility = is_tree_visible(rows, cols, row, col)
        expectedVisibility = True

        self.assertEqual(visibility, expectedVisibility)
    
    def test_is_tree_visible_inside_2(self):
        """
        Test is_tree_visible for edge
        """
        with open(self.INPUT_FILE,'r') as f:
            input_text = f.read()

        rows, cols = build_tree_rows_and_cols(input_text)

        row = 2
        col = 3

        visibility = is_tree_visible(rows, cols, row, col)
        expectedVisibility = False

        self.assertEqual(visibility, expectedVisibility)
