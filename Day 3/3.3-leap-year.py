# Get year.
year = int(input("Which year do you want to check? "))

# Write conditions for checking if given year is a leap year or not.

# Rule 1: If given year is evenly divisible by 4, check rule 2. // Else, print result. (Not leap year.)
# Rule 2: If given year is divisible by 100, check rule 3. // Else, print result. (Leap year.)
# Rule 3: If given year is divisible by 400, print result. (Leap year.) // Else, print result. (Not leap year.)

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")

# First attempt.

# if year % 4 == 0 and year % 100 != 0:
#   print("Leap year.")
# elif year % 4 == 0 and year % 100 == 0 and year % 400 ==0:
#   print("Leap year.")
# else:
#   print("Not leap year.")