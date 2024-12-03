"""
Scenarios for day {day}
"""

from common.scenario import Scenario

input="""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
output="7"
scenario = Scenario(input, output)
part_01_scenarios = [scenario]

input="""..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
output="336"
scenario = Scenario(input, output)
part_02_scenarios = [scenario]