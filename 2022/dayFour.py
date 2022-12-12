from .common import get_list_from_file

def main():
    pairs = get_list_from_file('day04-input.txt')
    
    overlaps = get_list_of_overlaps(pairs)

    print('There are ')

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

