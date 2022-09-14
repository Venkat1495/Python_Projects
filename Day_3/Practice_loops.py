# If loops
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?\n"))

if height >= 120 :
    print("you can ride the rollercoaster! (:")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("you have to pay $5 for ticket")
    elif (age >= 12 and age <=18) :
        print("you have to pay $7 for ticket")
    elif age > 18 :
        print("you have to pay $12 for ticket")

else:
    print("Sorry, you have to grow taller before you can ride.")


# Weather number input is odd or even

number = int(input("Which number do you want to check?\n"))

number_remainder = number % 2

if number_remainder == 0 :
    print("this is an even number.")
elif number_remainder == 1 :
    print("this is an odd number.")

# Nested If loops

