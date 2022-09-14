year = int(input("Which year do you want to check?"))

if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 :
    print(f"So year {year} is a leap year")
elif year % 4 == 0 and year % 100 != 0 :
    print(f"So year {year} is a leap year")
else :
    print(f"So year {year} is not a leap year")

# Roller Coaster ride with pics

print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?\n"))
price = 0
if height >= 120 :
    print("you can ride the rollercoaster! (:")
    age = int(input("What is your age?\n"))
    if age < 12:
        price = 5
        print(f"you have to pay ${price} for ticket")
    elif (age >= 12 and age <=18) :
        price = 7
        print(f"you have to pay ${price} for ticket")
    elif age >= 45 and age <= 55:
        price = 0
        print(f"you have to pay ${price} for ticket")
    elif age > 18 :
        price = 12
        print(f"you have to pay ${price} for ticket")

    photos = input(f"Do you want photos? Type 'yes' or 'no' : ")

    if photos == "yes" :
        price = price + 3
        print(f"The total bill is ${price}")
    else :
        print(f"The total bill is ${price}")

else:
    print("Sorry, you have to grow taller before you can ride.")


# Pizza Delivery App

print("Welcome to the python pizza Deliveries")

size = input("What size of pizza do you want? S,or M, or L : ").upper()

add_pepperoni = input("Do you want pepperoni? Y or N : ").upper()

extra_cheese = input("Do you want extra cheese? Y or N : ").upper()

Final_price = 0

if size == "S" :
    Final_price += 15
elif size == "M" :
    Final_price += 20
elif size == "L" :
    Final_price += 25

if add_pepperoni == "Y" and size == "S" :
    Final_price += 2
elif add_pepperoni == "Y" and size in {"M","L"} :
    Final_price += 3

if extra_cheese == "Y" :
    Final_price += 1

print(f"Your final bill is : {Final_price}")

# Love Calculator

print("Welcome to the Love Calculator!")

name_one = input("What is you name ?\n").upper()
name_two = input("What is their name ?\n").upper()

name = name_one + name_two

int_true = 0

int_true += name.count("T")
int_true += name.count("R")
int_true += name.count("U")
int_true += name.count("E")

int_love = 0

int_love += name.count("L")
int_love += name.count("O")
int_love += name.count("V")
int_love += name.count("E")

Final_love = int(str(int_true) + str(int_love))

if Final_love < 10 or Final_love > 90 :
    print(f"Your score is {Final_love}, you to together like coke and mentos")
elif Final_love >= 40 and Final_love <= 50 :
    print(f"Your score is {Final_love}, you are alright together")
else:
    print(f"Your score is {Final_love}.")