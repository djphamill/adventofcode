"""
aoc command start
"""
from argparse import ArgumentParser
from datetime import datetime

from commands.make import make
from commands.solve import solve

this_year = datetime.now().strftime('%Y')

class Year(int):

    def __str__(self):
        txt = super(int, self).__str__()
        return txt.zfill(4)

class Day(int):

    def __str__(self):
        txt = super(int, self).__str__()
        return txt.zfill(2)

def add_make_command(subparser: ArgumentParser) -> None:
    make_parser = subparser.add_parser("make", help="Make the files associated with a day's AOC")

    make_parser.add_argument("day", type=Day)

    make_parser.add_argument("-y", "--year", type=Year, default=this_year)
    
    make_parser.set_defaults(func=make)

def add_solve_command(subparser: ArgumentParser) -> None:
    solve_parser = subparser.add_parser("solve", help="Solve the given day's problem given the input")
    
    solve_parser.add_argument("input")

    solve_parser.add_argument("day", type=Day)
    
    solve_parser.add_argument("-y", "--year", type=Year, default=this_year)
    solve_parser.set_defaults(func=solve)

if __name__ == "__main__":
    args_parser = ArgumentParser(prog="aoc",
                                 description="A program to automate the create of files for adventofcode")
    subparser = args_parser.add_subparsers()
    add_make_command(subparser)
    add_solve_command(subparser)
    args = args_parser.parse_args()
    args.func(args)
