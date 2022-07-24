# Greeting.
print("Welcome to the Tip Calculator.")

# Total bill amount.
bill_val = float(input("What was the total bill? $"))

# Tip percentage.
tip_val = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_pct = tip_val / 100

# Bill including tip amount.
bill_incl_tip = bill_val * (1 + tip_pct)

# Split by number.
split_val = int(input("How many people to split the bill? "))
# split_bill = round(bill_incl_tip / split_val, 2)

# Use formatting to display 0's in decimals.
split_bill = "{:.2f}".format(bill_incl_tip / split_val, 2)

# Output message.
message = (f"Each person should pay: ${split_bill}")
print(message)