from _2023.day08 import *


def test_example_1_pt1():
    lines = ["RL",
             "",
             "AAA = (BBB, CCC)",
             "BBB = (DDD, EEE)",
             "CCC = (ZZZ, GGG)",
             "DDD = (DDD, DDD)",
             "EEE = (EEE, EEE)",
             "GGG = (GGG, GGG)",
             "ZZZ = (ZZZ, ZZZ)"]    
    expected = 2
    actual = pt1(lines)
    assert actual == expected
     
def test_example_2_pt1():
    lines = ["LLR",
             "",
             "AAA = (BBB, BBB)",
             "BBB = (AAA, ZZZ)",
             "ZZZ = (ZZZ, ZZZ)"]
    expected = 6
    actual = pt1(lines)
    assert actual == expected
    
    
def test_example_pt2():
    lines = ["LR",
             "",
             "11A = (11B, XXX)",
             "11B = (XXX, 11Z)",
             "11Z = (11B, XXX)",
             "22A = (22B, XXX)",
             "22B = (22C, 22C)",
             "22C = (22Z, 22Z)",
             "22Z = (22B, 22B)",
             "XXX = (XXX, XXX)",]
    expected = 6
    actual = pt2(lines)
    assert actual == expected