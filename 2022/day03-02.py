from string import ascii_lowercase, ascii_uppercase 

priorityValues = dict(zip(ascii_lowercase + ascii_uppercase, range(1,53)))

with open('day03-input.txt', 'r') as f:
    rucksacks = f.read().split('\n')

groups = [rucksacks[i : i+3] for i in range(0, len(rucksacks)-2, 3)]
priorities = []

for group in groups:
    rucksackA = group.pop()
    for item in rucksackA:
        if all([item in rucksack for rucksack in group]):
            priorities.append(priorityValues[item])
            break

assert len(priorities) == len(groups)
print(priorities[:5])
print(sum(priorities))
