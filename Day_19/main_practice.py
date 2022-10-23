from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
# Etch A Sketch APP
def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def counter_clockwise():
    tim.left(10)
def clockwise():
    tim.right(10)
def home():
    tim.home()
    tim.clear()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=home)
screen.exitonclick()