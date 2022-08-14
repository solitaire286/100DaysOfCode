student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Calculate the sum of all the elements within the student_heights list using a for loop.
total_height = 0

for height in student_heights:
  total_height += height

# Calculate the number of elements within the student_heights list using a for loop.
total_number = 0

for number in student_heights:
  total_number += 1

# Calculate the average height.
average_height = round(total_height / total_number)
print(average_height)