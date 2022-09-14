print("Welcome to the tip Calculator.")
total_bill = float(input("What was the total bill?\n"))
tip_percentage = int(input("What percentage tip would you like to give? like : 10, 12 or 15?\n"))
total_people = int(input("How many people to split the bill?\n"))

tip_percentage = 1 + (tip_percentage/100)
per_person = (total_bill * tip_percentage) / total_people
final_bill = "{:.2f}".format(round(per_person,2))
print(f"Each person should pay: $ {final_bill}")

