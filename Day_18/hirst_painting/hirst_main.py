import random
import turtle
from turtle import Turtle, Screen
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.hideturtle()
tim.up()
tim.setpos(-300, -300)
tim.down()
screen = Screen()

# Below is Colorgram code for random colors from painting
# import colorgram as cg
# colors = cg.extract('hirst-spot-pic.jpg', 20)
# color_list = []
#
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
def new_start_position():
    pos = tim.position()
    pos = list(pos)
    pos[0] -= 500
    pos[1] += 50
    tuple(pos)
    tim.up()
    tim.setpos(pos)
    tim.down()



color_list = [(216, 161, 77), (178, 56, 85), (232, 212, 104), (55, 102, 153), (211, 142, 176), (139, 104, 65), (105, 177, 211), (112, 187, 161), (220, 99, 76), (33, 57, 127), (153, 205, 225), (106, 108, 192), (74, 162, 96), (125, 39, 72), (92, 53, 40), (184, 78, 95)]

for j in range(10):
    for i in range(10):
        tim.dot(20, random.choice(color_list))
        tim.up()
        tim.forward(50)
    new_start_position()




screen.exitonclick()
