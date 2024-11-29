def main():
    with open('data/day04-input.txt', 'r') as f:
        pairs = f.read().split('\n')

    overlaps = get_list_of_overlaps(pairs)

    print(f'There are {sum(overlaps)} overlaps.')

def get_list_of_overlaps(pairs):
    overlaps = []

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
    
    return overlaps


if __name__ == "__main__":
    main()

