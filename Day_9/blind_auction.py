#HINT: You can call clear() to clear the output in the console.
import os
from art import logo
clear = lambda: os.system('clear')
print(logo)
print("Welcome to the secret auction program.")
is_true = True
bid_war = {}
while is_true:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_war[name] = bid
    yes = input("Are there any other bidders?Type 'yes' or 'no'.")
    if yes == 'yes':
        is_true = True
        clear()
    else:
        is_true = False
winner = ""
winner_bid = 0
for value in bid_war:
    if winner_bid <= bid_war[value]:
        winner_bid = bid_war[value]
        winner = value
print(f"The winner is {winner} with a bid of ${winner_bid}.")