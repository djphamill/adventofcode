from _2023.day06 import *


def test_example_pt1():
    lines = EXAMPLE
    actual = pt1(lines)
    expected = 288
    assert actual == expected
    
def test_example_pt2():
    lines = EXAMPLE
    actual = pt2(lines)
    expected = 71503
    assert actual == expected
    

EXAMPLE = ["Time:      7  15   30",
           "Distance:  9  40  200"]
