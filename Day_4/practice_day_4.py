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

# List

fruits = ["apple", "cherry", "Pear"]
print(fruits)
fruits[1] = "Banana"
print(fruits)
fruits.append("cherry")
print(fruits)

# Nester Lists

vegetables = ["Spinach", "Kale", "Tomtoes", "Celery"]

dirty_frozen = [fruits,vegetables]

print(dirty_frozen)

# Bill Paying person

name_str = input("Give me everybody's names, seperated by a comma.")
name = name_str.split(", ")
length = len(name)

random_name = random.randint(1,length) - 1
print(f"You are going to pay the bill : {name[random_name]}")

# Near Hundred

num = int(input("Please enter the any random number : "))

if (num >= 90 and num <= 110) or (num >= 190 and num <= 210) :
    print("true")
else:
    print("false")