############### Blackjack Project #####################
import random
from art import logo

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.t
def list_add(user_cards):
    score = 0
    for i in user_cards:
        score += i
    return score

def list_ace(user_cards):
    for i in user_cards:
        if i == 11 :
            index = user_cards.index(i)
            user_cards[index] = 1
    return user_cards
def final_print(my_cards, com_cards):
    my_score = list_add(my_cards)
    com_score = list_add(com_cards)
    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Computer's final hand: {com_cards}, final score: {com_score}")

def BalckJack():
    is_true = True

    while is_true:
        yes = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
        if yes == 'y':
            is_true = True
        else:
            break
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        my_cards = []
        com_cards = []
        my_cards.append(random.choice(cards))
        my_cards.append(random.choice(cards))
        com_cards.append(random.choice(cards))
        com_cards.append(random.choice(cards))
        my_score = list_add(my_cards)
        print(f"Your cards: {my_cards}, Current Score: {my_score}")
        print(f"Computer's first card : {com_cards[0]}")
        while True:
            another = input("Type 'y' to get another card, type 'n' to pass: ")
            if another == 'y':
                my_cards.append(random.choice(cards))
                my_score = list_add(my_cards)
                if my_score <= 21:
                    print(f"Your cards: {my_cards}, Current Score: {my_score}")
                    continue
                else:
                    my_cards = list_ace(my_cards)
                    my_score = list_add(my_cards)
                    if my_score > 21 :
                        break
                    elif my_score <= 21:
                        print(f"We changed your Ace card as it exceed score and Your cards: {my_cards}, Current Score: {my_score}")
                        continue
            else:
                break
        if my_score > 21 :
            final_print(my_cards,com_cards)
            print("You went over. You LOSE 😤")
            continue
        com_score = list_add(com_cards)
        while com_score <= 16:
            com_cards.append(random.choice(cards))
            com_score = list_add(com_cards)
        if com_score > 21 :
            final_print(my_cards,com_cards)
            print("Computer went over. So You WIN")
            continue
        if my_score > com_score:
            print("You WIN!!!")
        elif my_score < com_score:
            print("you LOSE 😤")
        elif my_score == com_score:
            print("you DRAW!!!!")


BalckJack()




