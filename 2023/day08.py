from numpy import lcm
import re
import sys
import time
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Node:
    id: str
    L: str
    R: str
    
    @property
    def is_zzz(self) -> bool:
        return self.id == 'ZZZ'
    
    @property
    def ends_with_z(self) -> bool:
        return  self.id[-1] == 'Z'
    
    @property
    def ends_with_a(self) -> bool:
        return  self.id[-1] == 'A'


def pt1(lines: List[str]) -> int:
    instructions = lines[0]
    nodes = get_nodes(lines)
    number_of_steps = find_number_of_steps(instructions, nodes)
    return number_of_steps

def get_nodes(lines: List[str]) -> Dict['str', Node]:
    nodes = {}
    for line in lines[2:]:
        id_, left, right = re.findall(r'[0-9A-Z]{3}', line)
        node = Node(id_, left, right)
        nodes.update({
            node.id: node
        })
    return nodes

def find_number_of_steps(instructions: List[str], nodes: Dict['str', Node]) -> int:
    at_zzz = False
    steps = 0
    node = Node('AAA', 'x', 'x')
    node_id = node.id
    while not at_zzz:
        for direction in instructions:
            node = nodes[node_id]
            node_id = getattr(node, direction)
            if node.is_zzz:
                at_zzz = True
                break
            steps += 1
    return steps

def pt2(lines: List[str]) -> int:
    instructions = lines[0]
    nodes = get_nodes(lines)
    step_counts = find_steps_to_node_ending_with_z(instructions, nodes)
    lowest_common_multiple = 1
    for next_number in step_counts:
        lowest_common_multiple = lcm(lowest_common_multiple, next_number)
    return lowest_common_multiple
    

def find_steps_to_node_ending_with_z(instructions: str,
                                      nodes: Dict['str', Node]) -> List[int]:
    step_counts = []
    nodes_starting_with_a = [v for v in nodes.values() if v.ends_with_a]
    for node_starting_with_a in nodes_starting_with_a:
        step_count = find_step_count(node_starting_with_a, nodes, instructions)
        step_counts.append(step_count)
    return step_counts

def find_step_count(node_starts_with_a: Node, nodes: List[Node], instructions: str) -> int:
    at_node_ending_in_z = False
    steps = 0
    node_id = node_starts_with_a.id
    while not at_node_ending_in_z:
        for direction in instructions:
            node = nodes[node_id]
            node_id = getattr(node, direction)
            if node.ends_with_z:
                at_node_ending_in_z = True
                break
            steps += 1
    return steps

if __name__ == '__main__':
    file_path = sys.argv[1]
    with open(file_path, 'r') as file:
        lines = file.read().strip().split('\n')

    start = time.time()
    print('=' * 10)
    print(f'Part 1: {pt1(lines)}')
    end = time.time()
    print('.' * 10)
    print(f'Part 1 took {end - start}')
    print('=' * 10)
    start = time.time()
    print(f'Part 2: {pt2(lines)}')
    end = time.time()
    print('.' * 10)
    print(f'Part 2 took {end - start}')
    print('=' * 10)