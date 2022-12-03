totalCalories = [0] 
numberOfElves = 0

with open('day01-input.txt', 'r') as f:
    inputs = f.read().split('\n')

for input in inputs:
    if input:
        totalCalories[-1] += int(input)
    else:
        totalCalories.append(0)

print(totalCalories[:10])
print(max(totalCalories))
