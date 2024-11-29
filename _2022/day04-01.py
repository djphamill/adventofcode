overlaps = []

with open('day04-input.txt', 'r') as f:
    pairs = f.read().split('\n')

for pair in pairs:
    assignments = pair.replace('-',',').split(',')
    firstAssignment = [int(assignments[i]) for i in [0,2]]
    lastAssignment = [int(assignments[i]) for i in [1,3]]
    if len(set(firstAssignment)) == 1 or len(set(lastAssignment)) == 1:
        overlaps.append(1)
    elif firstAssignment.index(min(firstAssignment)) == lastAssignment.index(max(lastAssignment)):
        overlaps.append(1)
    else:
        overlaps.append(0)

# Rough checks
assert max(overlaps) == 1 and min(overlaps) == 0
assert overlaps[:5] == [0, 0, 0, 1, 0]
assert overlaps[10] == 1
assert len(overlaps) == len(pairs)

print(f'There are {sum(overlaps)} pairs that overlap.')

