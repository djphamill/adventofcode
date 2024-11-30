from _2023.day10 import *
import pytest
from parameterized import parameterized

def test_example_1_pt1():
    lines = [
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF",
    ]
    actual = pt1(lines)
    expected = 4
    assert actual == expected
    
def test_example_2_pt1():
    lines = [
        "7-F7-",
        ".FJ|7",
        "SJLL7",
        "|F--J",
        "LJ.LJ",
    ]
    actual = pt1(lines)
    expected = 8
    assert actual == expected
    
@parameterized.expand([
    ('|', 3, 2, [(3, 1), (3, 3)]),
    ('-', 3, 2, [(4, 2), (2, 2)]),
    ('L', 3, 2, [(3, 1), (4, 2)]),
    ('J', 3, 2, [(3, 1), (2, 2)]),
    ('7', 3, 2, [(3, 3), (2, 2)]),
    ('F', 3, 2, [(4, 2), (3, 3)]),
])
def test_connection_resolve(shape, x, y, expected):
    tile = Tile(shape, x, y)
    actual = ConnectionResolver.connected_to(tile)
    assert actual == expected

@parameterized.expand([
    ([
        "7-F7-",
        ".FJ|7",
        "SJLL7",
        "|F--J",
        "LJ.LJ",
    ], (Tile('S', 0, 2), Tile('|', 0, 3))),
    ([
        "-L|F7",
        "7S-7|",
        "L|7||",
        "-L-J|",
        "L|-JF",
    ], (Tile('S', 1, 1), Tile('|', 1, 2)))
])
def test_find_first_tile(lines, expected):
    actual = find_first_tiles(lines)
    assert actual == expected

@parameterized.expand([
    ([
        "...........",
        ".S-------7.",
        ".|F-----7|.",
        ".||.....||.",
        ".||.....||.",
        ".|L-7.F-J|.",
        ".|..|.|..|.",
        ".L--J.L--J.",
        "..........."
    ], 4),
    ([
        "..........",
        ".S------7.",
        ".|F----7|.",
        ".||OOOO||.",
        ".||OOOO||.",
        ".|L-7F-J|.",
        ".|II||II|.",
        ".L--JL--J.",
        ".........."
    ], 4),
    ([
        "..........",
        ".S------7.",
        ".|F----7|.",
        "FJ|OOOO||.",
        "L7|OOOO||.",
        "FJL-7F-J|.",
        "L7II||II|.",
        ".L--JL--J.",
        ".........."
    ], 4),
    ([
        "F--------7",
        "|S------7|",
        "||F----7||",
        "|||OOOO|||",
        "LJ|OOOO|||",
        "F7L-7F-J||",
        "||II||II||",
        "|L--JL--J|",
        "L--------J"
    ], 4),
    ([
        "F--------7",
        "|.------7|",
        "||F----7||",
        "|||OOOO|||",
        "LJ|OOOO|||",
        "F7L-7F-J||",
        "||II||II||",
        "F---JL---7",
        "S--------J"
    ], 8),
    ([
        ".F----7F7F7F7F-7....",
        ".|F--7||||||||FJ....",
        ".||.FJ||||||||L7....",
        "FJL7L7LJLJ||LJ.L-7..",
        "L--J.L7...LJS7F-7L7.",
        "....F-J..F7FJ|L7L7L7",
        "....L7.F7||L7|.L7L7|",
        ".....|FJLJ|FJ|F7|.LJ",
        "....FJL-7.||.||||...",
        "....L---J.LJ.LJLJ..."
    ], 8),
    ([
        "FF7FSF7F7F7F7F7F---7",
        "L|LJ||||||||||||F--J",
        "FL-7LJLJ||||||LJL-77",
        "F--JF--7||LJLJ7F7FJ-",
        "L---JF-JLJ.||-FJLJJ7",
        "|F|F-JF---7F7-L7L|7|",
        "|FFJF7L7F-JF7|JL---7",
        "7-L-JL7||F7|L7F-7F7|",
        "L.L7LFJ|||||FJL7||LJ",
        "L7JLJL-JLJLJL--JLJ.L"
    ], 10)
])
@pytest.mark.xfail
def test_example_1_pt2(lines, expected):
    actual = pt2(lines)
    assert actual == expected

def test_inflate_map():
    lines = [
        "..........",
        ".S------7.",
        ".|F----7|.",
        ".||OOOO||.",
        ".||OOOO||.",
        ".|L-7F-J|.",
        ".|II||II|.",
        ".L--JL--J.",
        ".........."
    ]
    actual = inflate_map(lines)
    expected = [
        ".*.*.*.*.*.*.*.*.*.",
        "*******************",
        ".*S*-*-*-*-*-*-*7*.",
        "*******************",
        ".*|*F*-*-*-*-*7*|*.",
        "*******************",
        ".*|*|*O*O*O*O*|*|*.",
        "*******************",
        ".*|*|*O*O*O*O*|*|*.",
        "*******************",
        ".*|*L*-*7*F*-*J*|*.",
        "*******************",
        ".*|*I*I*|*|*I*I*|*.",
        "*******************",
        ".*L*-*-*J*L*-*-*J*.",
        "*******************",
        ".*.*.*.*.*.*.*.*.*.",
    ]
    assert actual == expected