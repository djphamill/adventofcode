"""
Scenarios for day {day}
"""

from common.scenario import Scenario

input="""3   4
4   3
2   5
1   3
3   9
3   3
"""
output="11"
scenario = Scenario(input, output)
part_01_scenarios = [scenario]

input="""3   4
4   3
2   5
1   3
3   9
3   3"""
output="31"
scenario = Scenario(input, output)
part_02_scenarios = [scenario]