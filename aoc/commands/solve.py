"""
Find the solution for that day/years AOC problem
Place input in to that solution
"""
from datetime import datetime

this_year = datetime.now().strftime('%Y')

def solve(input, day=None, year=this_year):
    print('solving problem')