import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Get user input.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Display user choice graphic.
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)
else:
  print("Please input a valid number.")

# Get computer to randomly select number between 0-1.
cpu_choice = random.randint(0, 2)

# Display computer choice graphic.
if cpu_choice == 0:
  print(f"Computer chose:\n{rock}")
elif cpu_choice == 1:
  print(f"Computer chose:\n{paper}")
elif cpu_choice == 2:
  print(f"Computer chose:\n{scissors}")








# Convert 0,1,2 to use corresponding varialbles.
# Computer should randomly select between range 0-2.
# Print computer choice. "Computer chose:"
# Write conditionals for the following;
# If both user and computer pick same option, result = draw.
# If user = 0 (rock), computer = 1 (paper), result = computer wins (paper > rock)
# If user = 1 (paper), computer = 2 (scissors), result = computer wins (scissors > paper)
# If user = 2 (scissors), computer = 0 (rock), result = computer wins (rock > scissors)
