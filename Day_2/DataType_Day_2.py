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