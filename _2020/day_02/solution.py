"""
Solution to day 02
"""
import re
from collections import Counter

def solution_part_01(input: str) -> str:
    lines = [line.strip() for line in input.split('\n') if line]

    line_pattern = r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$'
    total_valid_password = 0
    for line in lines:
        match = re.match(line_pattern, line)
        least_occurences = int(match[1])
        most_ocurrences = int(match[2])
        letter_to_check = match[3]
        password = match[4]

        counter = Counter(password)
        count_for_letter = counter[letter_to_check]
        if count_for_letter < least_occurences or count_for_letter > most_ocurrences:
            continue
        total_valid_password += 1
    return str(total_valid_password)

def solution_part_02(input: str) -> str:
    lines = [line.strip() for line in input.split('\n') if line]

    line_pattern = r'^(\d+)-(\d+) ([a-z]): ([a-z]+)$'
    total_valid_passwords = 0
    for line in lines:
        match = re.match(line_pattern, line)
        first_position = int(match[1]) - 1
        second_position = int(match[2]) - 1
        letter_to_check = match[3]
        password = match[4]

        is_letter_in_first_position = password[first_position] == letter_to_check
        is_letter_in_second_position = password[second_position] == letter_to_check

        if not is_letter_in_first_position and not is_letter_in_second_position:
            continue
        if is_letter_in_first_position and is_letter_in_second_position:
            continue
        total_valid_passwords += 1
    return str(total_valid_passwords)