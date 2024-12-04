"""
Scenarios for day {day}
"""

from common.scenario import Scenario

input="""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
output="18"
scenario = Scenario(input, output)
part_01_scenarios = [scenario]

input=""".M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
.........."""
output="9"
scenario = Scenario(input, output)
part_02_scenarios = [scenario]