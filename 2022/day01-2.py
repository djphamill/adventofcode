totalCalories = [0]

with open('day01-input.txt', 'r') as f:
    inputs = f.read().split('\n')

for input in inputs:
    if input:
        totalCalories[-1] += int(input)
    else:
        totalCalories.append(0)

sortedTotaCalories = sorted(totalCalories, reverse=True)

print(sortedTotaCalories[:10])
print(sum(sortedTotaCalories[:3]))
