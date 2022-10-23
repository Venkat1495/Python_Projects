import random
from turtle import Turtle,Screen


def move_start_position(color, y):
    toy = Turtle(shape="turtle")
    toy.penup()
    toy.color(color)
    toy.goto(x=-230, y=y)
    return toy


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
ys = [-150, -100, -50, 0, 50, 100]
names = []
for i in range(0,6):
    new_turtle = move_start_position(colors[i], ys[i])
    names.append(new_turtle)
if user_bet:
    is_true = True

while is_true:
    for turtle in names:
        if turtle.xcor() > 230:
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You won! The {wining_color} turtle is the winner")
            else:
                print(f"You Lost! The {wining_color} turtle is the winner")
            is_true = False

        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)

screen.exitonclick()