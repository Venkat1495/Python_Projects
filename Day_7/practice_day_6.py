# Step 1
import random

stages = ['''
You have '0' lives
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
You have '1' live
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
You have '2' lives
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
You have '3' lives
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
You have '4' lives
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
You have '5' lives
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
You have '6' lives
  +---+
  |   |
      |
      |
      |
      |
=========
''']

user_word = []
lives = 6

word_list = ["ardvark", "baboon", "camel"]

random_word_int = random.randint(0, len(word_list) - 1)

chosen_word = word_list[random_word_int]

print(f"passt, the solution is {chosen_word}.")

for i in chosen_word:
    user_word.append("_")

print(user_word)

while True:
    letter = input("Guess a letter: ").lower()
    j = 0
    k = 0
    for i in chosen_word:
        if i.lower() == letter:
            user_word[j] = i
            k += 1
        j += 1
    if k == 0:
        lives -= 1
    print(user_word)
    print(stages[lives])
    if "_" in user_word and lives == 0:
        print("you loss (:, Try Again")
        break
    elif "_" in user_word:
        continue
    else:
        print("you win :)")
        break






