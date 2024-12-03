"""
Solution to day 02
"""
from typing import List

def solution_part_01(input: str) -> str:
    lines = [line.strip().split(" ") for line in input.split('\n') if line]
    
    reports = []
    for line in lines:
        report = [int(level) for level in line] 
        reports.append(report)

    for report in reports:
        pass

def is_always_increasing(report: List[int]) -> bool:
    return sorted(report) == report

def is_always_decreasing(report: List[int]) -> bool:
    return sorted(report, reverse=True) == report

def is_difference_tolerable(report: List[int]) -> bool:
    first_numbers = report[:-1]
    second_numbers = report[1:]
    for first_number, second_number in zip(first_numbers, second_numbers):
        absolute_difference = abs(first_number - second_number)
        if absolute_difference < 1:
            return False
        if absolute_difference > 3:
            return False
    return True

def solution_part_02(input: str) -> str:
    pass