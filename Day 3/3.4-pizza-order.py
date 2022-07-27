# Greeting.
print("Welcome to Python Pizza Deliveries!")

# Get size of pizza.
size = input("What size pizza do you want? S, M, or L ")

# Price of pizza based on size. $15 (S), $20 (M), $25 (L)
# Price of extra toppings based on size. Pepperoni: +$2 (S), +3$ (M/L) // Cheese: $1 (Any)

# If small pizza.
if size == "S":
  bill = 15
  add_pepperoni = input("Do you want pepperoni? Y or N ")
  if add_pepperoni == "Y":
    bill += 2
  extra_cheese = input("Do you want extra cheese? Y or N ")
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}")
# If medium pizza.
elif size == "M":
  bill = 20
  add_pepperoni = input("Do you want pepperoni? Y or N ")
  if add_pepperoni == "Y":
    bill += 3
  extra_cheese = input("Do you want extra cheese? Y or N ")
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}")
# If large pizza.
elif size == "L":
  bill = 20
  add_pepperoni = input("Do you want pepperoni? Y or N ")
  if add_pepperoni == "Y":
    bill += 3
  extra_cheese = input("Do you want extra cheese? Y or N ")
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}")
  
