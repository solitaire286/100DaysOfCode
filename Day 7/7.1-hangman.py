# Hangman v1.0

word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random
chosen_word = random.choice(word_list)

# Ask the user to guess a letter and assign their letter to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for char in chosen_word:
    if char == guess:
        print("Yes")
    else:
        print("No")