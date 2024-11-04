with open("day1/input.txt", "r") as file:
    data = file.readlines()

elfCaloriesList = []
calories = 0
for line in data:
    if (line == '\n'):
        elfCaloriesList.append(calories)
        calories = 0
    else:    
        calories += int(line)

elfCaloriesList = sorted(elfCaloriesList, reverse=True) 

print(sum(elfCaloriesList[:1]))
print(sum(elfCaloriesList[:3]))