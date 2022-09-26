# Function with Inputs  ////// Agr === Value ////  parameter is ===== like variables , name /////
import math


def greet(x):
    print(f"The Name is")
    print(f"{x}")
    print(f"And My name is Venkat! Hi.........")

name = input("What is your FullName: ")
location = input("Please let us know your location: ")
#greet(name)

# Functions with more than one inputs
def greet_with(name, location):
    print(f"Your name is : {name}")
    print(f"your location is :  {location}")

#greet_with(location = location, name = name)

# Key Word Arguments a = 1, b = 2, c = 3 even if change the order it is still the same like above.

#Write your code below this line 👇
def paint_calc(height, cover, width):
    paints = (height * width) / cover
    paints = math.ceil(paints)
    print(f"you will need {paints} cans of paint.")


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
"""
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
"""
# Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
        if number == 2 :
            is_prime = True
    if number == 0 or number == 1 :
        is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)