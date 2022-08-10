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

# Get computer to randomly pick a number between 0-2.
cpu_choice = random.randint(0, 2)

# Display computer choice graphic.
if cpu_choice == 0:
  print(f"Computer chose:\n{rock}")
elif cpu_choice == 1:
  print(f"Computer chose:\n{paper}")
elif cpu_choice == 2:
  print(f"Computer chose:\n{scissors}")

# Define rules for "Draw".
if cpu_choice == user_choice:
  print("It's a draw!")

# Define rules for "Win/Lose".
elif user_choice == 0 and cpu_choice == 1:
  print("Paper covers rock. You lose!")
elif user_choice == 1 and cpu_choice == 2:
  print("Scissors cut paper. You lose!")
elif user_choice == 2 and cpu_choice == 0:
  print("Rock breaks scissors. You lose!")

elif cpu_choice == 0 and user_choice == 1:
  print("Paper covers rock. You win!")
elif cpu_choice == 1 and user_choice == 2:
  print("Scissors cut paper. You win!")
elif cpu_choice == 2 and user_choice == 0:
  print("Rock breaks scissors. You win!")