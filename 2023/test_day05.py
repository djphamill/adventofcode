from day05 import *
from parameterized import parameterized
from pytest_check import check



def test_example_pt1():
    lines = EXAMPLE
    actual = pt1(lines)
    expected = 35
    assert actual == expected

@parameterized.expand([
    (0, 0),
    (1, 1),
    (48, 48),
    (49, 49),
    (50, 52),
    (51, 53),
    (96, 98),
    (97, 99),
    (98, 50),
    (99, 51),
])
def test_example_seed_to_soil(seed, expected):
    map = {
        tuple([98, 99]): tuple([50, 51]),
        tuple([50, 97]): tuple([52, 99]),
    }
    actual = get_destination(seed, map)
    assert actual == expected

def test_get_seeds_with_ranges():
    seeds_lines = ['seeds: 12 3 20 1 100 5']
    actual = list(get_seeds_with_ranges(seeds_lines))
    expected = [12, 13, 14, 20, 100, 101, 102, 103, 104]
    assert actual == expected
    
def test_get_seeds():
    lines = EXAMPLE
    actual = get_seeds(lines)
    expected = [79, 14, 55, 13]
    assert actual == expected
    
def test_get_map_lines():
    lines = EXAMPLE
    actual = get_map_lines(lines)
    expected = [EXAMPLE[2:5],
                EXAMPLE[6:10],
                EXAMPLE[11: 16],
                EXAMPLE[17:20],
                EXAMPLE[21:25],
                EXAMPLE[26:29],
                EXAMPLE[30:33]]
    assert actual == expected

@parameterized.expand([
    ('mid group', 12, 2),
    ('pre groups', 2, 2),
    ('in between groups', 18, 18),
    ('start of group', 5, 101),
    ('end of group', 8, 104),
    ('singleton group', 20, 6)
])
def test_get_destination(_, source, expected):
    map_source_to_destination = {
        tuple([5, 8]): tuple([101, 104]),
        tuple([11, 15]): tuple([1, 5]),
        tuple([20, 20]): tuple([6, 6]),
    }
    actual = get_destination(source, map_source_to_destination)
    assert actual == expected
    
def test_build_map():
    lines = ["abc-to-wxyz map:",
             "10 12 3",
             "101 2 12",
             "0 9 3",
             "1 1 1",
             "17 25 5"]
    actual_source, actual_destination, actual_map = build_map(lines)
    expected_source = 'abc'
    expected_destination = 'wxyz'
    expected_map = {
        tuple([12, 14]): tuple([10, 12]),
        tuple([2, 13]): tuple([101, 112]),
        tuple([9, 11]): tuple([0, 2]),
        tuple([1, 1]): tuple([1, 1]),
        tuple([25, 29]): tuple([17, 21]),
    }
    with check:
        assert actual_source == expected_source
        assert actual_destination == expected_destination
        assert actual_map == expected_map

EXAMPLE = ["seeds: 79 14 55 13",
           "",
           "seed-to-soil map:",
           "50 98 2",
           "52 50 48",
           "",
           "soil-to-fertilizer map:",
           "0 15 37",
           "37 52 2",
           "39 0 15",
           "",
           "fertilizer-to-water map:",
           "49 53 8",
           "0 11 42",
           "42 0 7",
           "57 7 4",
           "",
           "water-to-light map:",
           "88 18 7",
           "18 25 70",
           "",
           "light-to-temperature map:",
           "45 77 23",
           "81 45 19",
           "68 64 13",
           "",
           "temperature-to-humidity map:",
           "0 69 1",
           "1 0 69",
           "",
           "humidity-to-location map:",
           "60 56 37",
           "56 93 4"]