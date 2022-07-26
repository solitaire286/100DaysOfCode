# Get height and weight.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

# Calculate BMI based on height and weight. (Round the result to the nearest whole number.)
bmi = round(weight / height ** 2)

# Write conditions for different weight categories.
# Below 18.5: underweight / Above 18.5 but below 25: normal weight / Above 25 but below 30: slightly overweight. / Above 30 but below 35: obese / Above 35: clinically obese

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")