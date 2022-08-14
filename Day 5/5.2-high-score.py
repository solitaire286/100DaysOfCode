student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Calculate the highest score from the 'student_scores' list using a for loop.
highest_score = 0

# Loop through the list and update the highest score candidate if a score is greater than it.
for score in student_scores:
  if score > highest_score:
    highest_score = score

print(f"The highest score in the class is: {highest_score}")