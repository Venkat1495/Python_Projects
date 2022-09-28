# Dictionary

# {key: value}

programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running",
    "report": "The results of the bug",
    "loop": "The action of doing something over and over again"
}
# Retrieving
print(programming_dictionary["Bug"])

#Adding new items
programming_dictionary["Function"] = "The call group of code again and again"

print(programming_dictionary)

# Create new empty dictionary

empty_dic = {}

# Wipe existing dictionary

#programming_dictionary = {}

# print(programming_dictionary)

# edit item in dictionary

programming_dictionary["Bug"] = "An issue that comes will doing testing"

print(programming_dictionary)

# Loop through the dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])