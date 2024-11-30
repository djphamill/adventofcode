"""
Class to represent a numbered day in aoc
"""

class Day(int):

    def __str__(self):
        txt = super(int, self).__str__()
        return txt.zfill(2)
