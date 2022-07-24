# Get current age.
age = input("What is your current age? ")

# Number of years left.
years_left = 90 - int(age)

# How many days, weeks, and months remain from a 90 year life. (1 Year = 365 Days, 52 Weeks, 12 Months)
days = years_left * 365
weeks = years_left * 52
months = years_left * 12

# Output message.
message = (f"If you made it to 90, you have {days} days, {weeks} weeks, and {months} months left.")
print(message)