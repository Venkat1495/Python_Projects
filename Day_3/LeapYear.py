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