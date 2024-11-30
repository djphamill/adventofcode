"""
Solution to day 01
"""
from itertools import combinations
from math import prod

def solution_part_01(input: str) -> str:
    numbers = [int(line.strip()) for line in input.split('\n')]
    number_pairs = combinations(numbers, 2)
    for pair in number_pairs:
        if sum(pair) == 2020:
            return str(prod(pair))

def solution_part_02(input: str) -> str:
    numbers = [int(line.strip()) for line in input.split('\n')]
    number_pairs = combinations(numbers, 3)
    for pair in number_pairs:
        if sum(pair) == 2020:
            return str(prod(pair))