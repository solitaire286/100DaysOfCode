# Greeting.
print("Welcome to the Love Calculator!")

# Get names.
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combine both names into a single string and convert to lower case for use with the count() method.
lower_case_names = (name1 + " " + name2).lower()

# Count the number of times the letters, TRUE and LOVE occur in the combined names.
count_true_in_names = lower_case_names.count('t') + lower_case_names.count('r') + lower_case_names.count('u') + lower_case_names.count('e')
count_love_in_names = lower_case_names.count('l') + lower_case_names.count('o') + lower_case_names.count('v') + lower_case_names.count('e')

# Calculate the combined love score.
love_score = int(str(count_true_in_names) + str(count_love_in_names))

# Output message based on combined love score.
if love_score <= 10 or love_score >= 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")