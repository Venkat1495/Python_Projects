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
