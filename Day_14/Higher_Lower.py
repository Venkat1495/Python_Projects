# To-Do
# Display Logo
# Display 2 print statements
# Comparing the 2 Variables
# Adding the score for correct ans
# displaying the final score
import random

# Imports
from art import logo
from art import vs
from game_data import data

# Global Variables
score = 0
char_a = random.randint(0, (len(data) - 1))
char_b = random.randint(0, (len(data) - 1))


def diff_int(char_a, char_b):
    is_true = True
    while is_true:
        if char_a == char_b:
            char_b = random.randint(0, (len(data) - 1))
        else:
            is_true = False


def ran_names(char_a, char_b):
    print(
        f"Compare A: {data[char_a]['name']}, a {data[char_a]['description']}, from {data[char_a]['country']} and ANS Insta Followers : {data[char_a]['follower_count']} ")
    print(vs)
    print(
        f"Against B: {data[char_b]['name']}, a {data[char_b]['description']}, from {data[char_b]['country']} and ANS Insta Followers : {data[char_b]['follower_count']} ")


def score_logic():
    if data[char_a]['follower_count'] > data[char_b]['follower_count']:
        return char_a
    else:
        return char_b


def High_Low():
    global score
    global char_a
    global char_b
    print(logo)
    while True:
        ran_names(char_a, char_b)
        ans_char = score_logic()
        user_ans = input("Who has more followers? Type 'A' or 'B': ")
        if user_ans == 'A' and ans_char == char_a:
            score += 1
            print(f"You're right! Current score: {score}")
        elif user_ans == 'B' and ans_char == char_b:
            score += 1
            print(f"You're right! Current score: {score}")
            char_a = char_b
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
        char_b = random.randint(0, (len(data) - 1))
        diff_int(char_a, char_b)


diff_int(char_a, char_b)
High_Low()
