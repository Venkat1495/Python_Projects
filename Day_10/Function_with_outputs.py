def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"{f_name} {l_name}"
f_name = input("Please type your first name: ")
l_name = input("Please type your last name: ")
full_name = format_name(f_name, l_name)
print(full_name)