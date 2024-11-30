"""
Class to encapsualte a partt of the day's problem
"""

class Part(int):
    " Represent a part of the day's problem"

    def __new__(cls, obj):
        value = int.__new__(cls, obj)
        if value not in [1, 2]:
            raise TypeError("Part can only be 1 or 2")
        return value