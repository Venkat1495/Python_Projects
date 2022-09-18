# For loop with using list
def forlearn() :
    fruit = ["apple", "mango", "orange"]
    for i in fruit :
        print(i)

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



# My function calling
# forlearn()
average_height()