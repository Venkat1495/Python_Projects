def format_name(f_name, l_name):
    """It takes first and last name, and returns them in the Tittle format"""
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"
f_name = input("Please type your first name: ")
l_name = input("Please type your last name: ")
full_name = format_name(f_name,l_name)
print(full_name)

def is_leap(year):
    """Returns whether the passed year is leap year or not"""
    year #= int(input("Which year do you want to check?"))

    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
def days_in_month(year, month):
    is_true = is_leap(year)
    month -= 1
    month_days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = month_days[month]
    if is_true and days == 28:
        days += 1
    return days

# Do Not Change below code checking the push after making it private again

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# DoStrings : it is definition of a function displayed when we call the function. and it is defined the first function

