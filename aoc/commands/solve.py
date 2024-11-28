"""
Find the solution for that day/years AOC problem
Place input in to that solution
"""
from datetime import datetime

this_year = datetime.now().strftime('%Y')

def solve(args):
    day, year = args.day, args.year
    print('solving problem')