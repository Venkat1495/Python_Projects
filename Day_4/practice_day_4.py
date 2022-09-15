import random
random_int = random.randint(1,10)
print(random_int)

random_float = random.random()
print(random_float)

print(random_float * 5) # So we will get the random float numbers from 0 to 4.9999 in between based on the number we mutiply

# Head or Tail Coin Toss

print("Welcome to the Coin Toss Helper.")

toss = input("When you are ready, please press Y/N,").lower()

toss_int = random.randint(1,2)

if toss == "y" :
    if toss_int == 1 :
        print("Head")
    elif toss_int == 2 :
        print("Tail")
    else:
        print("Please choose the correct option")
else:
    print("Thanks for showing interest")

