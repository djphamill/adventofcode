"""
Solution to day 01
"""
from collections import Counter

def solution_part_01(input: str) -> str:
    lines = [line.strip() for line in input.split('\n') if line]
    unordered_pairs = [line.split() for line in lines]

    first_set = []
    second_set = []
    for first, second in unordered_pairs:
        first_set.append(first)
        second_set.append(second)
    sorted_first_set = sorted(first_set)
    sorted_second_set = sorted(second_set)

    absolute_differences = []
    for first, second in zip(sorted_first_set, sorted_second_set):
        absolute_differences.append(abs(int(first) - int(second)))

    return str(sum(absolute_differences))

def solution_part_02(input: str) -> str:
    lines = [line.strip() for line in input.split('\n') if line]
    unordered_pairs = [line.split() for line in lines]

    first_list = []
    second_counter= Counter()
    for first, second in unordered_pairs:
        first_list.append(first)
        second_counter.update([int(second)])
    
    total = 0
    for number in first_list:
        total += int(number) * int(second_counter[int(number)])
    return str(total)