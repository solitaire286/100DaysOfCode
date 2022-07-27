# Greeting.
print("Welcome to Python Pizza Deliveries!")

# Get pizza size.
size = input("What size pizza do you want? S, M, or L ")

# Get extra toppings.
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

# Price of pizza. $15 (S), $20 (M), $25 (L)
# Price of extra toppings. Pepperoni: +$2 (S), +3$ (M/L) // Cheese: $1 (Any)

# If small pizza.
if size == "S":
  bill = 15
  if add_pepperoni == "Y":
    bill += 2
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")
# If medium pizza.
elif size == "M":
  bill = 20
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")
# If large pizza.
elif size == "L":
  bill = 25
  if add_pepperoni == "Y":
    bill += 3
  if extra_cheese == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}.")

# Angela's Solution.
# bill = 0

# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25

# if add_pepperoni == "Y":
#   if size == "S":
#     bill += 2
#   else:
#     bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is: ${bill}.")