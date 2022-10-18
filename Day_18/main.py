import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
tim = Turtle()
# Challenge 3 Different Shape
# colors = ["spring green", "blue", "light sky blue", "red", "magenta", "blue violet", "indian red"]
# tim.shape("turtle")
# for i in range(3,10):
#     tim.color(random.choice(colors))
#     for j in range (0, i):
#         tim.forward(100)
#         tim.right(360/i)

# Challenge 4 Random Walk and getting random colour


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# rotate_dic_list = [ "same", "rt_night", "lt_night", "about_turn"]
# tim.shape("arrow")
# tim.speed("fastest")
# tim.pensize(10)
# for i in range(201):
#     tim.color(random_color())
#     rotate_choice = random.choice(rotate_dic_list)
#     if rotate_choice == "same" :
#         tim.right(0)
#     elif rotate_choice == "rt_night":
#         tim.right(90)
#     elif rotate_choice == "lt_night":
#         tim.left(90)
#     elif rotate_choice == "about_turn":
#         tim.right(180)
#     tim.forward(20)

# Challenge 5 : Draw a circle with a tilt
tim.shape("arrow")
tim.speed("fastest")
for i in range(0, 360, 5):
    tim.color(random_color())
    tim.setheading(i)
    tim.circle(100)

# Challenge 2 : Dashed line
# is_true = True
# for i in range(1 ,50):
#     tim.forward(10)
#     if is_true:
#         tim.up()
#         is_true = False
#     else:
#         tim.down()
#         is_true = True

screen = Screen()
screen.exitonclick()