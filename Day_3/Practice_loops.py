# If loops
print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm?\n"))

if height >= 120 :
    print("you can ride the rollercoaster! (:")
else:
    print("Sorry, you have to grow taller before you can ride.")


# Weather number input is odd or even

number = int(input("Which number do you want to check?\n"))

number_remainder = number % 2

if number_remainder == 0 :
    print("this is an even number.")
elif number_remainder == 1 :
    print("this is an odd number.")
