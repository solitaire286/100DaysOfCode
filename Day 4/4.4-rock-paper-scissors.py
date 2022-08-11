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

game_gfx = [rock, paper, scissors]

# Get user input.
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Get computer to randomly pick a number between 0-2.
cpu_choice = random.randint(0, 2)

# Give error message and stop, if user enters anything other than 0, 1, or 2.
if user_choice >= 3 or user_choice < 0:
  print("You entered an invalid number, you lose!")

else:
  # Display user choice graphic.
  print(game_gfx[user_choice])

  # Display computer choice graphic.
  print(f"Computer chose:\n{game_gfx[cpu_choice]}")

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

# # Angela's solution.

# # Capture invalid input.
# if user_choice >= 3 or user_choice < 0:
#   print("You typed an invalid number, you lose!")
# # Capture Rock > Scissors (0 > 2) outcome.
# elif user_choice == 0 and cpu_choice == 2:
#   print("You win!")
# elif cpu_choice == 0 and user_choice == 2:
#   print("You lose")
# # Capture general outcomes for Scissors > Paper > Rock (2 > 1 > 0)
# elif user_choice > cpu_choice:
#   print("You win!")
# elif cpu_choice > user_choice:
#   print("You lose")
# # Capture outcome for a draw.
# elif cpu_choice == user_choice:
#   print("It's a draw")