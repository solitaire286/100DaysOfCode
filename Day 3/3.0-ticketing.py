# Get height.
height = int(input("What is your height (cm)? "))

# If height >= 120, allow access to ride. // Else, print result. ("Sorry, come back when you're taller.")
if height >= 120:
  print("You can ride the rollercoaster!")
  # Get age and create ticket variations based on same.
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Enjoy a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")

  # Get confirmation if user wants a photo taken and add it to final bill. // Else, print result. ("Enjoy your ride!")
  photo = input("Do you want a photo taken? Y or N. ")
  if photo == "Y":
    bill += 3
    print(f"Your final bill is, ${bill}.\nEnjoy your ride!")
  else:
    print("Enjoy your ride!")

else:
  print("Sorry, come back when you're taller.")