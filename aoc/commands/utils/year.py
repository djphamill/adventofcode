"""
Class to represent aoc years
"""

class Year(int):

    def __str__(self):
        txt = super(int, self).__str__()
        return txt.zfill(4)
