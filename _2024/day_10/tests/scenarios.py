"""
Scenarios for day {day}
"""

from common.scenario import Scenario

input="""0123
1234
8765
9876"""
output="1"
scenario = Scenario(input, output)
part_01_scenarios = [scenario]
input="""...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9"""
output="2"
scenario = Scenario(input, output)
part_01_scenarios.append(scenario)
input="""10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01"""
output="3"
scenario = Scenario(input, output)
part_01_scenarios.append(scenario)
input="""89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
output="36"
scenario = Scenario(input, output)
part_01_scenarios.append(scenario)

input="""<paste here>"""
output="<paste here>"
scenario = Scenario(input, output)
part_02_scenarios = [scenario]