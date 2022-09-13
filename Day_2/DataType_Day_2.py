# Data Types

# Strings

print("Hello"[-1]) # Subscripting

# Interger

print(123 + 1_34_356)

# Float

print(3.14159)

# Boolean

print(True & False)

# type check

print(type(3.14159))

# type convertions int to str

print(type(str(11_23_450)))

# Code Challenge

two_digit_number = input("Type any two digit number : ")
two_digit_number = list(two_digit_number)
final_digit = 0
for i in two_digit_number:
    digit_x = int(i)
    final_digit = final_digit + int(digit_x)

print(final_digit)

# Mathematical Operations

# 3 + 4
# 5 - 7
# 8 * 5
print(6 / 2) # it will float always
print(6 ** 2)

# PEMDAS (), **, *, /, +, -

# BMI Calucator

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = weight / (height ** 2)
BMI = round(BMI)

print(BMI)

# Remaining Days

age = int(input("What is your current age?"))

years_remaining = 90 - age
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365
months_remaining = years_remaining * 12

print(f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")
