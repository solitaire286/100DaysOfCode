# Get height and weight, and convert into numerical value.
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))

# Calculate BMI and output as an integer value.
bmi = int(weight / (height ** 2))

# Print BMI.
print(bmi)