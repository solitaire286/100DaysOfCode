# Greeting.
print("Welcome to the Love Calculator!")

# Get names.
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Concatenate both names into a single string and convert to lower case for use with the count() method.
joint_names = (name1 + " " + name2).lower()

# Count the number of times the letters, TRUE and LOVE occur in the combined names string.
count_true = joint_names.count('t') + joint_names.count('r') + joint_names.count('u') + joint_names.count('e')
count_love = joint_names.count('l') + joint_names.count('o') + joint_names.count('v') + joint_names.count('e')

# Calculate the combined love score.
love_score = int(str(count_true) + str(count_love))

# Output message based on combined love score.
if love_score <= 10 or love_score >= 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")