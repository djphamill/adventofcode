import unittest
from ..dayFour import get_list_of_overlaps

class TestDay04(unittest.TestCase):
    """
    Test functions created for Day04 tasks
    """

    def testGetOverLapsOnePair(self):
        """
        Test get_list_of_overlaps for one pair and they overlap
        """
    
        overlaps = get_list_of_overlaps(['2-3,3-4'])
        expected = [1]
        self.assertEqual(overlaps, expected)

    def testGetOverlpasNoOverlap(self):
        """
        Test get_list_of_overlaps with multiple pairs, none of which overlap
        """

        overlaps = get_list_of_overlaps([
            '1-2,3-4',
            '9-10,99-100',
            '12-22,0-1'
        ])
        expected = [0,0,0]
        self.assertEqual(overlaps, expected)
    
    def testGetOverlapsMultiple(self):
        """
        Test get_list_of_overlaps with multple pairings of different types
        """

        overlaps = get_list_of_overlaps([
            '1-2,3-4', # No overlap, 0
            '9-10,10-100', # Overlap, 1
            '12-22,12-21', # Overlap, 1
            '4-10,7-10', # Overlap, 1
            '48-55,5-8' # No overlap, 0
        ])
        expected = [0, 1, 1, 1, 0]
        self.assertEqual(overlaps, expected)