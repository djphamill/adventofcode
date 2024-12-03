"""
Solution to day 03
"""
from math import prod
import re
from typing import Tuple

def solution_part_01(input: str) -> str:
    lines = [line.strip() for line in input.split('\n') if line]

    multiply_pattern = re.compile(r'mul\((\d{0,3}),(\d{0,3})\)')
    total = 0
    for line in lines:
        matches = multiply_pattern.findall(line)
        for match in matches:
            integers = [int(integer) for integer in match]
            total += prod(integers)
    return str(total)


def solution_part_02(input: str) -> str:
    lines = [line.strip() for line in input.split('\n') if line]

    matching_pattern = re.compile(r"mul\((\d{0,3}),(\d{0,3})\)|(do\(\))|(don't\(\))")
    total = 0
    is_enabled = True
    for line in lines:
        matches = matching_pattern.findall(line)
        for match in matches:
            if is_match_for_multiplication(match) and is_enabled:
                integers = [int(integer) for integer in match[:2]]
                total += prod(integers)
            elif should_disable(match):
                is_enabled = False
            elif should_enable(match):
                is_enabled = True
    return str(total)

def is_match_for_multiplication(match: Tuple[str]) -> bool:
    return bool(match[0]) and bool(match[1])

def should_enable(match: Tuple[str]) -> bool:
    return bool(match[2])

def should_disable(match: Tuple[str]) -> bool:
    return bool(match[3])