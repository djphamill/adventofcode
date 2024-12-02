"""
Scenarios for day {day}
"""

from common.scenario import Scenario

input="""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
output="2"
scenario = Scenario(input, output)
part_01_scenarios = [scenario]

input="""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
output="1"
scenario = Scenario(input, output)
part_02_scenarios = [scenario]