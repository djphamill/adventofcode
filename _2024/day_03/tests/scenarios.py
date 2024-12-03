"""
Scenarios for day {day}
"""

from common.scenario import Scenario

input="""xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""
output="161"
scenario = Scenario(input, output)
part_01_scenarios = [scenario]

input="""xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""
output="48"
scenario = Scenario(input, output)
part_02_scenarios = [scenario]