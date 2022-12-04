overlaps = []

with open('day04-input.txt', 'r') as f:
    pairs = f.read().split('\n')

for pair in pairs:
    assignments = pair.replace('-',',').split(',')
    firstAssignment = [int(assignments[i]) for i in [0,2]]
    lastAssignment = [int(assignments[i]) for i in [1,3]]

    # If the first or last assignments are the same, there is definite overlap
    if len(set(firstAssignment)) == 1 or len(set(lastAssignment)) == 1:
        overlaps.append(1)
        continue
    
    elfWithHighestFirstAssignment = firstAssignment.index(max(firstAssignment))
    otherElf = 0 if elfWithHighestFirstAssignment == 1 else 1

    if firstAssignment[elfWithHighestFirstAssignment] <= lastAssignment[otherElf]:
        overlaps.append(1)
    else:
        overlaps.append(0)



# Rough checks
assert max(overlaps) == 1 and min(overlaps) == 0
assert 0 in overlaps
assert len(overlaps) == len(pairs)
assert overlaps[:5] == [1, 1, 1, 1, 1]
assert overlaps[20] == 0


print(f'There are {sum(overlaps)} pairs that overlap.')

