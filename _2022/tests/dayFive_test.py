import unittest
from _2022.dayFiveOne import top_of_each_stack, stacks_after_move, split_into_stacks_moves_strings, build_move_dict, build_stacks_list
from _2022.dayFiveTwo import stacks_after_move_maintain_order

class TestDayFive(unittest.TestCase):
    """
    Tests for the functions defined in the solution for Day Five task
    """

    def test_top_of_each_stack_(self):
        """
        Test top_of_each_stack function
        """

        top_crates = top_of_each_stack([['a','b','c'],['z','y'],['z'],['f','h','f','h','i']])
        expected_top_crates = 'cyzi'

        self.assertEqual(top_crates, expected_top_crates)

    def test_stacks_after_move_two_stacks(self):
        """
        Test stacks_after_move with two stacks passed in and only one move to perform
        """
        stacks_before_move = [['A', 'X', 'F', 'W'], ['R', 'S', 'T']]
        move = {
            'number': 2,
            'from': 2,
            'to': 1
        }
        
        stacks = stacks_after_move(stacks_before_move, move)
        expectedStacks = [['A', 'X', 'F', 'W', 'T', 'S'], ['R']]

        self.assertEqual(stacks, expectedStacks)
    
    def test_stacks_after_move_three_stacks(self):
        """
        Test stacks_after_move with two stacks passed in and only one move to perform
        """
        stacks_before_move = [['A', 'X', 'F', 'W'], ['R', 'S', 'T'], ['D', 'M', 'N']]
        move ={
            'number': 4,
            'from': 1,
            'to': 3
        }
        
        stacks = stacks_after_move(stacks_before_move, move)
        expectedStacks = [[], ['R', 'S', 'T'], ['D', 'M', 'N', 'W', 'F', 'X', 'A']]

        self.assertEqual(stacks, expectedStacks)


    def test_split_into_stacks_moves_strings(self):
        """
        Test split_into_stacks_moves_stringss
        """
        string_list = [
            '        [O]    ',
            '        [E] [R]',
            '    [F] [V] [L]',
            '[Z] [X] [E] [P]',
            '1   2   3   4', 
            '', 
            'move 1 from 2 to 1',
            'move 3 from 3 to 4',
            'move 1 from 4 to 2',
            'move 5 from 4 to 3'
        ]
        stacks_strings, moves_strings = split_into_stacks_moves_strings(string_list)
        expected_stacks = [
            '        [O]    ',
            '        [E] [R]',
            '    [F] [V] [L]',
            '[Z] [X] [E] [P]'
        ]
        expected_moves = [
            'move 1 from 2 to 1',
            'move 3 from 3 to 4',
            'move 1 from 4 to 2',
            'move 5 from 4 to 3'
        ]

        self.assertEqual(stacks_strings, expected_stacks)
        self.assertEqual(moves_strings, expected_moves)

    def test_build_move_dict(self):
        """
        Test build_moves_dict
        """

        move_string = "move 13 from 100 to 878"
        move = build_move_dict(move_string)
        expected_move = {
            'number': 13,
            'from': 100,
            'to': 878
        }

        self.assertEqual(move, expected_move)

    def test_build_stacks_list(self):
        """
        Test build_stacks_list
        """

        stacks_strings = [
            '        [O]    ',
            '        [E] [R]',
            '    [F] [V] [L]',
            '[Z] [X] [E] [P]'
        ]

        stacks = build_stacks_list(stacks_strings)
        expected_stacks = [['Z'], ['X', 'F'], ['E', 'V', 'E', 'O'], ['P', 'L', 'R']]
        
        self.assertEqual(stacks, expected_stacks)

    def test_stacks_after_move_maintain_order(self):
        """
        Test stacks_after_move_maintain_order
        """
        stacks_before_move = [['A', 'X', 'F', 'W'], ['R', 'S', 'T'], ['D', 'M', 'N']]
        move ={
            'number': 4,
            'from': 1,
            'to': 3
        }
        
        stacks = stacks_after_move_maintain_order(stacks_before_move, move)
        expectedStacks = [[], ['R', 'S', 'T'], ['D', 'M', 'N', 'A', 'X', 'F', 'W']]

        self.assertEqual(stacks, expectedStacks)

        