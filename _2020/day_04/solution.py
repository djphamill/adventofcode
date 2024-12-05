"""
Solution to day 04
"""
import re
from typing import Callable

Birth_Year = "byr"
Issue_Year = "iyr"
Expiration_Year = "eyr"
Height = "hgt"
Hair_Color = "hcl"
Eye_Color = "ecl"
Passport_ID = "pid"
Country_ID = "cid"

class Field:

    def __init__(self, field_name: str, validator: Callable):
        self._field_name = field_name
        self._validator = validator
    
    def __str__(self) -> str:
        return self._field_name

    def is_valid(self, value: str) -> bool:
        return self._validator(value)

def is_four_digits(value: str) -> bool:
    is_four_digits = len(value) == 4 and value.isdigit()
    if not is_four_digits:
        return False
    return True

def birth_year_validator(value: str) -> bool:
    if not is_four_digits(value):
        return False
    is_right_value = int(value) >= 1920 and int(value) <= 2002
    if not is_right_value:
        return False
    return True

def issue_year_validator(value: str) -> bool:
    if not is_four_digits(value):
        return False
    is_right_value = int(value) >= 2010 and int(value) <= 2020
    if not is_right_value:
        return False
    return True

def expiration_year_validator(value: str) -> bool:
    if not is_four_digits(value):
        return False
    is_right_value = int(value) >= 2020 and int(value) <= 2030
    if not is_right_value:
        return False
    return True

def height_validator(value: str) -> bool:
    is_number_with_cm = bool(re.match(r'^\d+cm', value))
    if is_number_with_cm:
        number = int(re.findall(r'^(\d+)cm', value)[0])
        if number <= 150 and number >= 193:
            return False
        return True

    is_number_with_in = bool(re.match(r'^\d+in', value))
    if is_number_with_in:
        number = int(re.findall(r'^(\d+)in', value)[0])
        if number <= 59 and number >= 76:
            return False
        return True

    return False

def eye_color_validator(value: str) -> bool:
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def hair_color_validator(value: str) -> bool:
    match = re.match("^#[a-f0-9]{6}", value)
    if not match:
        return False
    return True

def passport_id_validator(value: str) -> bool:
    match = re.match("^[0-9]{9}", value)
    if not match:
        return False
    return True

required_fields = [Field(Birth_Year, birth_year_validator),
                   Field(Issue_Year, issue_year_validator),
                   Field(Expiration_Year, expiration_year_validator),
                   Field(Height, height_validator),
                   Field(Hair_Color, hair_color_validator),
                   Field(Eye_Color, eye_color_validator),
                   Field(Passport_ID, passport_id_validator)]

pattern_template = '{field}:(\S+)'

def solution_part_01(input: str) -> str:
    sections = [section.replace('\n', ' ') for section in input.split('\n\n') if section]

    valid_passport_count = 0
    for section in sections:
        is_required_field_missing = False
        for required_field in required_fields:
            pattern = pattern_template.format(field=required_field)
            match = re.search(pattern, section)
            if not match:
                is_required_field_missing = True
                break
        if not is_required_field_missing:
            valid_passport_count += 1

    return str(valid_passport_count)


def solution_part_02(input: str) -> str:
    sections = [section.replace('\n', ' ') for section in input.split('\n\n') if section]

    valid_passport_count = 0
    for section in sections:
        is_required_field_missing_or_invalid = False
        for required_field in required_fields:
            pattern = pattern_template.format(field=required_field)
            match = re.findall(pattern, section)
            if not match:
                is_required_field_missing_or_invalid = True
                break

            if not required_field.is_valid(match[0]):
                is_required_field_missing_or_invalid = True
                break

        if not is_required_field_missing_or_invalid:
            valid_passport_count += 1

    return str(valid_passport_count)