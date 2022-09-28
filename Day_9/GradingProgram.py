student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

for socres in student_scores:
    if student_scores[socres] > 90 and student_scores[socres] <= 100:
        student_grades[socres] = "Outstanding"
    elif student_scores[socres] > 80 and student_scores[socres] <= 90:
        student_grades[socres] = "Exceeds Expectations"
    elif student_scores[socres] > 70 and student_scores[socres] <= 80:
        student_grades[socres] = "Acceptable"
    elif student_scores[socres] <= 70:
        student_grades[socres] = "Fail"

# TODO-2: Write your code below to add the grades to student_grades.👇


# 🚨 Don't change the code below 👇
print(student_grades)