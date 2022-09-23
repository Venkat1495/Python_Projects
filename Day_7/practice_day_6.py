# Step 1
import random

user_word = []

word_list = ["ardvark", "baboon", "camel"]

random_word_int = random.randint(0, len(word_list) - 1)

chosen_word = word_list[random_word_int]

print(f"passt, the solution is {chosen_word}.")

letter = input("Guess a letter: ").lower()

for i in chosen_word:
    user_word.append("_")

j = 0
for i in chosen_word:
    if i.lower() == letter:
        user_word[j] = i

    j += 1
print(user_word)
