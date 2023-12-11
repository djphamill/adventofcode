import sys
import time
from typing import List
from numpy.linalg import inv, solve
from numpy import mat, matrix, matmul, array

class Sequence:
    def __init__(self, sequence: List[int]):
        self.sequence = sequence
        self.number_of_terms = len(sequence)
        self._next_term = None
        self.differences = self.find_differences(sequence)

    @staticmethod
    def find_differences(sequence: List[str]) -> List[int]:
        differences = []
        for n, t_n in enumerate(sequence[:-1]):
            t_n_plus_1 = sequence[n + 1]
            differences.append(t_n_plus_1 - t_n)
        return differences

    @property
    def next_term(self) -> int:
        if self._next_term is not None:
            return self._next_term    
        
        common_difference = self.differences[0] if len(set(self.differences)) == 1 else None
        last_term = self.sequence[-1]
        if common_difference:
            self._next_term = last_term + common_difference
            return self._next_term

        sequence_of_differeces = Sequence(self.differences)
        self._next_term = last_term + sequence_of_differeces.next_term
        return self._next_term


def pt1(lines: List[str]) -> int:
    sequences = []
    for line in lines:
        sequences.append(Sequence([int(t) for t in line.split(' ')]))
    return sum([s.next_term for s in sequences])

def pt2(lines: List[str]) -> int:
    sequences = []
    for line in lines:
        sequences.append(Sequence([int(t) for t in line.split(' ')][::-1]))
    return sum([s.next_term for s in sequences])

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