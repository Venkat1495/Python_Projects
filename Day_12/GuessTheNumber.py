# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100.
# Pssst, the correct answer is 34
# Choose a difficulty. Type 'easy' or 'hard':
# You have 10 attempts remaining to guess the number.
#
#

import random
from art import logo
# ******** Global Variables *************
com_number = random.randint(1,101)

def number_logic(user_number):
    if user_number > com_number:
        print("Too high.")
        return 1
    elif user_number < com_number:
        print("Too Low.")
        return 1
    elif user_number == com_number:
        print(f"You got it! The answer was {com_number}.")
        return 0
    else:
        print("Please choose the correct value in next try. Thanks")
        return 1

def main_logic(difficulty):
    if difficulty == 'easy':
        i = 10
    else:
        i = 5
    for n in range(i, 0, -1):
        print(f"You have {n} attempts remaining to guess the number.")
        user_number = int(input("Make a guess: "))
        is_number = number_logic(user_number)
        if is_number == 0:
            break
        elif is_number == 1:
            if n > 1:
                print("Guess again.")
            else:
                print("You've run out of guesses, you lose.")
            continue






def main_guess():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pssst, the correct answer is {com_number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    main_logic(difficulty)
main_guess()
