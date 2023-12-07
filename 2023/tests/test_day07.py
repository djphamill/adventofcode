from day07 import *
from copy import copy
from parameterized import parameterized

EXAMPLE = ["32T3K 765",
           "T55J5 684",
           "KK677 28",
           "KTJJT 220",
           "QQQJA 483"]

def test_example_pt1():
    lines = copy(EXAMPLE)
    actual = pt1(lines)
    expected = 6440
    assert actual == expected
    
def test_example_pt2():
    lines = copy(EXAMPLE)
    actual = pt2(lines)
    expected = 5905
    assert actual == expected
    
@parameterized.expand([
    ('full house to high', "AAAAA", "12345", False),
    ('high to one pair', "23456", "22JKQ", True),
    ('one pair to two pair', "A2QQ5", "QQKKA", True),
    ('three kind to higher three kind', "8JJJQK", "KJJJ72", True),
    ('higher high to high', "65432", "23456", False),
    ('higher high on last card to high', "65437", "65432", False)
])
def test_hand_comparison_less_than(_, left, right, expected):
    left_hand, right_hand = Hand(left, 1), Hand(right, 1)
    actual = left_hand < right_hand
    assert actual == expected

@parameterized.expand([
    ('full house to high', "AAAAA", "12345", True),
    ('high to one pair', "23456", "22JKQ", False),
    ('one pair to two pair', "A2QQ5", "QQKKA", False),
    ('three kind to higher three kind', "8JJJQK", "KJJJ72", False),
    ('higher high to high', "65432", "23456", True),
    ('higher high on last card to high', "65437", "65432", True)
])
def test_hand_comparison_greater_than(_, left, right, expected):
    left_hand, right_hand = Hand(left, 1), Hand(right, 1)
    actual = left_hand > right_hand
    assert actual == expected
    
@parameterized.expand([
    (HandType.FIVE_OF_A_KIND, "AAAAA", 7),
    (HandType.HIGH_CARD, "12345", 1),
    (HandType.HIGH_CARD,"12345", 1),
    (HandType.ONE_PAIR, "11JKQ", 2),
    (HandType.ONE_PAIR, "12QQ5", 2),
    (HandType.TWO_PAIR, "QQKKA", 3),
    (HandType.THREE_OF_A_KIND, "8JJJQK", 4),
    (HandType.THREE_OF_A_KIND, "KJJJ12", 4),
    (HandType.FOUR_OF_A_KIND, "59999", 6),
    (HandType.FULL_HOUSE, "55999", 5)
])
def test_get_hand_type_rank(_, hand, expected):
    actual = Hand(hand, 99).type_rank
    assert actual == expected
