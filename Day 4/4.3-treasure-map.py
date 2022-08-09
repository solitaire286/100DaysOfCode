# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

position_x = int(position[1])
position_y = int(position[0])

map[position_x - 1][position_y - 1] = "X"

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")