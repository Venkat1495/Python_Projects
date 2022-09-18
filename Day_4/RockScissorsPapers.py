import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

RPS = [rock, paper, scissors]

our_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors : "))

print(RPS[our_choose])

cmp_choose = random.randint(0,2)

print(f"Computer Chose : \n \n {RPS[cmp_choose]}")

if our_choose == 0 and cmp_choose == 2 :
    print("You Win!")
elif our_choose == 2 and cmp_choose == 1 :
    print("You Win!")
elif our_choose == 1 and cmp_choose == 0 :
    print("You Win!")
elif our_choose == 2 and cmp_choose == 0 :
    print("You Lose!")
elif our_choose == 1 and cmp_choose == 2 :
    print("You Lose!")
elif our_choose == 0 and cmp_choose == 1 :
    print("You Lose!")
elif our_choose == cmp_choose :
    print("It's a draw")
