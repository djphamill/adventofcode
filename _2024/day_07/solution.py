"""
Solution to day 07
"""
from dataclasses import dataclass
import itertools
from typing import List, Generator, Callable

@dataclass
class Equation:
    test: int
    operands: List[int]

    @staticmethod
    def load(line: str):
        test, operands = line.split(':')
        
        operands = [int(operand) for operand in operands.split() if operand]
        return Equation(int(test), operands)

def solution_part_01(input: str) -> str:
    _allowed_operations = [add, prod]
    lines = [line.strip() for line in input.split('\n') if line]

    equations = [Equation.load(line) for line in lines]

    possibly_true_equations: List[Equation] = []
    for equation in equations:
        found_working_combination = False
        combinations_of_operations = get_combinations_of_operations(equation.operands, _allowed_operations)
        for combination_of_operations in combinations_of_operations:
            first_operand = equation.operands[0]
            for second_operand_index, operation in enumerate(combination_of_operations, start=1):
                second_operand = equation.operands[second_operand_index]
                first_operand = operation(first_operand, second_operand)
            total = first_operand
            if total == equation.test:
                found_working_combination = True
                break
        if found_working_combination:
            possibly_true_equations.append(equation)
    
    return str(sum([equation.test for equation in possibly_true_equations]))

def get_combinations_of_operations(operands: List[int], allowed_operations: List[Callable]) -> Generator[List[Callable], None, None]:
    number_of_operations = len(operands) - 1

    return itertools.product(allowed_operations, repeat=number_of_operations)

def add(first: int, second: int) -> int:
    return first + second

def prod(first: int, second: int) -> int:
    return first * second

def concatenate(first: int, second: int) -> int:
    concatenated = str(first) + str(second)
    return int(concatenated)

def solution_part_02(input: str) -> str:
    _allowed_operations = [add, prod, concatenate]
    lines = [line.strip() for line in input.split('\n') if line]

    equations = [Equation.load(line) for line in lines]

    possibly_true_equations: List[Equation] = []
    for equation in equations:
        found_working_combination = False
        combinations_of_operations = get_combinations_of_operations(equation.operands, _allowed_operations)
        for combination_of_operations in combinations_of_operations:
            first_operand = equation.operands[0]
            for second_operand_index, operation in enumerate(combination_of_operations, start=1):
                second_operand = equation.operands[second_operand_index]
                first_operand = operation(first_operand, second_operand)
            total = first_operand
            if total == equation.test:
                found_working_combination = True
                break
        if found_working_combination:
            possibly_true_equations.append(equation)
    
    return str(sum([equation.test for equation in possibly_true_equations]))