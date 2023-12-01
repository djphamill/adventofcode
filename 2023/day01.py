import sys 
import re

words_to_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

words_to_digits_pattern ='(' + ')|('.join(list(words_to_digits.keys())) + ')'

file_path = sys.argv[1]
with open(file_path, 'r') as file:
    lines = file.read().split('\n')

calibration_values = []
for line in lines:
    if line:
        match_exists = True
        while match_exists:
            match = re.search(words_to_digits_pattern, line)
            if not match:
                break
            line = line[:match.start()] + words_to_digits[match[0]] + line[match.start() + 1:]

        letters_pattern =r'[a-z]'
        calibration_value = int(re.sub(letters_pattern, '', line)[0] + re.sub(letters_pattern, '', line)[-1])
        
        calibration_values.append(calibration_value)

print(sum(calibration_values))