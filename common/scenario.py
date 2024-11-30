"""
Define test scenarios
"""

from dataclasses import dataclass

@dataclass
class Scenario:
    input: str
    output: str