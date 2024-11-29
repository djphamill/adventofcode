from string import ascii_lowercase, ascii_uppercase 

priorityValues = dict(zip(ascii_lowercase, range(1,27)))
priorityValues.update(dict(zip(ascii_uppercase, range(27,53))))

with open('day03-input.txt', 'r') as f:
    rucksacks = f.read().split('\n')

priorities = []

for rucksack in rucksacks:
    compSize = int(len(rucksack) / 2)
    compA = rucksack[:compSize]
    compB = rucksack[compSize:]

    for item in compA:
        if item in compB:
            priorities.append(priorityValues[item])
            break

assert len(priorities) == len(rucksacks)
print(priorities[:5])
print(sum(priorities))
