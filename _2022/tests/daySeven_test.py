import unittest
import pytest
import json
from _2022.daySevenOne import build_files_dict

@pytest.mark.xfail
class TestDay07(unittest.TestCase):
    """
    Test functions created for Day04 tasks
    """

    INPUT_FULE = '/Users/djph/Library/Mobile Documents/com~apple~CloudDocs/repos/adventofcode/2022/data/daySeven-input-test-03.txt'

    @pytest.mark.xfail
    def test_build_files_dict(self):
        """
        Test build_folder_tree
        """

        with open(self.INPUT_FULE, 'r') as f:
            commands = f.read().split('\n')

        files = build_files_dict(commands)
        expected_files = {
            'home/abc': 123,
            'home/xyz': 567,
            'home/x/rst' : 789,
            'home/x/X': 561,
            'home/x/y/jj': 200,
            'home/x/y/j.json': 100,
            'home/x/y/tut': 10,
            'home/x/ty/rs/pop.dat': 111,
            'home/z/hij.txt': 555,
            'home/z/uv.py': 777,
            'home/z/a': 909
        }

        self.assertEqual(len(files.keys()), len(expected_files.keys()))

        for key, value in files.items():
            self.assertTrue(expected_files[key]==value)
