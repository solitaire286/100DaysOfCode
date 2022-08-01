import random

# Split string method.
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Count number of elements in list.
names_count = len(names)

# Pick random name from list using count as range.
pick_name = names[random.randrange(0, names_count)]

# Output message.
print(f"{pick_name} is going to buy the meal today!")