"""
Solution to day 10
"""
from copy import deepcopy
from dataclasses import dataclass, field
from typing import Set, List
from pairing import pair

HEIGHTS = [str(height) for height in range(8, -1, -1)]

DOWN = [0, 1]
RIGHT = [1, 0]
UP = [0, -1]
LEFT = [-1 , 0]

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

@dataclass
class Point:
    right: int
    down: int
    char: str

    def __hash__(self) -> int:
        return pair(self.right, self.down)


@dataclass
class Base:
    right: int
    down: int
    char: str
    nines: Set[Point] = field(default_factory=set)
    
    def add_nine(self, nine: Point) -> None:
        self.nines.add(nine)
    
    @property
    def score(self) -> int:
        return len(self.nines)
    
    def __hash__(self) -> int:
        return pair(self.right, self.down)
    
    @staticmethod
    def build_from_adjacent_base(base: 'Base', point: Point) -> 'Base':
        return Base(point.right, point.down, point.char, base.nines)

class Map:

    def __init__(self, lines: List[str]) -> 'Map':
        self._lines = lines
        self._points = None

    def __iter__(self):
        if self._points:
            return iter(list(self._points.values()))
        
        points = {}
        for down, row in enumerate(self._lines):
            for right, char in enumerate(row):
                points.update({(right, down): Point(right, down, char)})
        self._points = points
        return iter(list(self._points.values()))
    
    def get_point(self, right, down) -> None | Point:
        point: Point = self._points.get((right, down), None)
        return point

def solution_part_01(input: str) -> str:
    lines = [line.strip() for line in input.split('\n') if line]
    map = Map(lines)

    points_of_nines = find_all_nines(map)
    base_of_trees = [Base(loc.right, loc.down, "9", set([loc])) for loc  in points_of_nines]
    for height in HEIGHTS:
        new_bases_of_trees = set()
        for base_of_tree in base_of_trees:
            next_bases = find_next_bases(height, base_of_tree, map)
            for base in next_bases:
                new_bases_of_trees.add(base)
        base_of_trees = deepcopy(new_bases_of_trees)
    
    return str(sum([base.score for base in base_of_trees]))
       

def find_all_nines(map: Map) -> Set[Point]:
    nines = set()
    for point in map:
        if point.char == "9":
            nines.add(Point(point.right, point.down, point.char)) 
    return nines

def find_next_bases(height: str, base_of_tree: Base, map: Map) -> Set[Base]:
    next_bases = set()
    for delta_right, delta_down in DIRECTIONS:
        adjacent_point: Point = map.get_point(right=base_of_tree.right + delta_right,
                                       down=base_of_tree.down + delta_down)
        if not adjacent_point or adjacent_point.char != height:
            continue
        next_base = Base.build_from_adjacent_base(base_of_tree, adjacent_point)
        next_bases.add(next_base)
        
    return next_bases

def solution_part_02(input: str) -> str:
    pass