import unittest
from ..dayNineOne import adjacency_and_alignment, is_ontop, build_as_single_moves, change_position, make_move
from ..dayNineTwo import build_new_moves

class TestDay09(unittest.TestCase):
    """
    Test functions created for Day04 tasks
    """

    def test_build_as_single_moves(self):
        
        moves = ['U 2', 'D 3', 'U 1', 'R 9', 'L 5']
        single_moves = build_as_single_moves(moves)

        expected_single_moves = ['U', 'U', 'D', 'D', 'D', 'U', 'R', 'R', 'R', 'R',
                                    'R', 'R', 'R', 'R', 'R', 'L', 'L', 'L', 'L', 'L']

        self.assertEqual(single_moves, expected_single_moves)
    
    def test_is_adjacent_head_on_top(self):
        positions = {
            'H': [3,5],
            'T': [3,4]
        }

        adjacent, alignment = adjacency_and_alignment(positions)
        self.assertTrue(adjacent)
        self.assertEqual(alignment, 'U')
    
    def test_is_adjacent_head_on_bottom(self):
        positions = {
            'H': [-1,-11],
            'T': [-1,-10]
        }

        adjacent, alignment = adjacency_and_alignment(positions)
        self.assertTrue(adjacent)
        self.assertEqual(alignment, 'D')
    
    def test_is_adjacent_head_to_left(self):
        positions = {
            'H': [8,2],
            'T': [7,2]
        }

        adjacent, alignment = adjacency_and_alignment(positions)
        self.assertTrue(adjacent)
        self.assertEqual(alignment, 'R')
    
    def test_is_adjacent_head_diagonal(self):
        positions = {
            'H': [3,7],
            'T': [4,8]
        }

        adjacent, alignment = adjacency_and_alignment(positions)
        self.assertFalse(adjacent)
        self.assertEqual(alignment, 'LD')
    
    def test_is_adjacent_head_far_away(self):
        positions = {
            'H': [-2,1],
            'T': [0,0]
        }

        adjacent, alignment = adjacency_and_alignment(positions)
        self.assertFalse(adjacent)
        self.assertEqual(alignment, 'LLU')
    
    def test_is_adjacent_head_ontop(self):
        positions = {
            'H': [-2,1],
            'T': [-2,1]
        }

        adjacent, alignment = adjacency_and_alignment(positions)
        self.assertFalse(adjacent)
        self.assertEqual(alignment, 'ONTOP')

    def test_is_ontop_when_ontop(self):
        positions = {
            'H': [3, 4],
            'T': [3, 4]
        }

        self.assertTrue(is_ontop(positions))

    def test_is_ontop_when_not_ontop(self):
        positions = {
            'H': [-1 ,0],
            'T': [0, -1]
        }

        self.assertFalse(is_ontop(positions))
    
    def test_change_position_left_with_head(self):
        positions = {
            'H': [-1 ,0],
            'T': [0, -1]
        }

        positions = change_position(positions, 'L', 'H')

        expected_postions = {
            'H': [-2 ,0],
            'T': [0, -1]
        }
        self.assertDictEqual(positions, expected_postions)

    def test_change_position_down_with_tail(self):
        positions = {
            'H': [2, 2],
            'T': [3, 10]
        }

        positions = change_position(positions, 'D', 'T')

        expected_postions = {
            'H': [2, 2],
            'T': [3, 9]
        }
        self.assertDictEqual(positions, expected_postions)
    
    def test_change_position_up_with_tail(self):
        positions = {
            'H': [2, 2],
            'T': [3, 10]
        }

        positions = change_position(positions, 'U', 'T')

        expected_postions = {
            'H': [2, 2],
            'T': [3, 11]
        }
        self.assertDictEqual(positions, expected_postions)

    def test_make_move_diagonal_LD(self):
        positions = {
            'H': [2, 3],
            'T': [3, 4]
        }

        move = 'R'

        expected_positions = {
            'H': [3, 3],
            'T': [3, 4]
        }

        positions = make_move(move, positions)

        self.assertDictEqual(positions, expected_positions)
    
    def test_make_move_diagonal_UL_out_more(self):
        positions = {
            'H': [2, 5],
            'T': [3, 4]
        }

        move = 'L'

        expected_positions = {
            'H': [1, 5],
            'T': [2, 5]
        }

        positions = make_move(move, positions)

        self.assertDictEqual(positions, expected_positions)

    def test_make_move_on_top_down(self):
        positions = {
            'H': [-1, 0],
            'T': [-1, 0]
        }

        move = 'D'

        expected_positions = {
            'H': [-1, -1],
            'T': [-1, 0]
        }

        positions = make_move(move, positions)

        self.assertDictEqual(positions, expected_positions)

    def test_make_move_left_over_tail(self):
        positions = {
            'H': [0, 4],
            'T': [-1, 4]
        }

        move = 'L'

        expected_positions = {
            'H': [-1, 4],
            'T': [-1, 4]
        }

        positions = make_move(move, positions)

        self.assertDictEqual(positions, expected_positions)
    
    def test_make_move_left_and_pull_tail(self):
        positions = {
            'H': [0, 4],
            'T': [1, 4]
        }

        move = 'L'

        expected_positions = {
            'H': [-1, 4],
            'T': [0, 4]
        }

        positions = make_move(move, positions)

        self.assertDictEqual(positions, expected_positions)

    def test_make_move_down_and_pull_tail(self):
        positions = {
            'H': [10, 4],
            'T': [10, 5]
        }

        move = 'D'

        expected_positions = {
            'H': [10, 3],
            'T': [10, 4]
        }

        positions = make_move(move, positions)

        self.assertDictEqual(positions, expected_positions)

    def test_make_move_up_and_ontop(self):
            positions = {
                'H': [0, -1],
                'T': [0, 0]
            }

            move = 'U'

            expected_positions = {
                'H': [0, 0],
                'T': [0, 0]
            }

            positions = make_move(move, positions)

            self.assertDictEqual(positions, expected_positions)

    def test_build_new_moves(self):
        motion = [[0,0], [1,0], [2,0], [2,-1], [3,-2], [3,-1], 
                    [3,-2], [3,-1], [3,0], [3,1], [2,1]]

        new_moves = build_new_moves(motion)

        expected_new_moves = ['R', 'R', 'D', 'RD', 'U', 'D', 'U', 'U', 'U', 'L']

        self.assertEqual(new_moves, expected_new_moves)