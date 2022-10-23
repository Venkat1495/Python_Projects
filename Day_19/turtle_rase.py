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

for i in range(0,6):
    toy = move_start_position(colors[i], ys[i])
screen.exitonclick()