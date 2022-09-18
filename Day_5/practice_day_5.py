# For loop with using list
def forlearn() :
    fruit = ["apple", "mango", "orange"]
    for i in fruit :
        print(i)

    number = 0

    for n in range(0,101, 1) :
        number += n

    print(number)


def average_height() :
    student_h = input("Input a list of student heights ").split()
    i = 0
    sum = 0
    for n in student_h : # you can give name for n in singular form
        student_h[i] = int(n)
        i += 1
        sum += int(n)

    average = round(sum / i)
    print(average)

def max_score() :
    student_h = input("Input a list of student scores").split()
    temp = "0"
    i_max = "0"
    for score in student_h:  # you can give name for n in singular form

        if int(score) > int(temp) :
            i_max = int(score)
            temp = score



    print(f"The highest score in the clase is: {i_max}")


# My function calling
forlearn()
# average_height()
# max_score()