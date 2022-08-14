# Calculate the sum of all the even numbers from 1 to 100. (i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100)
total = 0

for number in range(0, 101, 2):
  total += number
print(total)

# Alternate solution 1
total = 0

for number in range(2, 101, 2):
  total += number
print(total)

# Alternate solution 2
total = 0

for number in range(0, 101):
  if number % 2 == 0:
    total += number
print(total)