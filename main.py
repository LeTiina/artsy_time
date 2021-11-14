import colorgram
from turtle import Turtle,Screen
import random

colors = colorgram.extract('truniokuva.jpg',20)
list_of_colors = []
for i in range(0, 20):
    color = colors[i]
    rgb = color.rgb
    red = rgb[0]
    green = rgb[1]
    blue = rgb[2]
    tuple_for_the_list = (red, green, blue)
    list_of_colors.append(tuple_for_the_list)

timmy_the_painter = Turtle()
screen = Screen()
screen.colormode(255)
timmy_the_painter.penup()
timmy_the_painter.goto(-250,-250)
timmy_the_painter.speed(500)


def draw_line():
    x = 0
    while x < 10:
        random_color = random.randrange(0, 20)
        timmy_the_painter.pencolor(list_of_colors[random_color])
        timmy_the_painter.pendown()
        timmy_the_painter.dot(20)
        timmy_the_painter.penup()
        timmy_the_painter.forward(50)
        x += 1


a = 0
position = -200
while a < 10:
    draw_line()
    timmy_the_painter.penup()
    timmy_the_painter.goto(-250,position)
    a += 1
    position += 50

screen.exitonclick()
