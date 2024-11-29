"""
Constants used in aoc program
"""
import os
import re

utils_path, _ = os.path.split(__file__)
project_path_pattern = r".*/adventofcode"
match = re.match(project_path_pattern, utils_path)
project_path = match.group(0)
