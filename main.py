import turtle

import colorgram
from turtle import Turtle,Screen

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

print(list_of_colors)
#10*10 rows of spots
#dot 20 in size
#space between 50

timmy_the_painter = Turtle()
timmy_the_painter.penup()
timmy_the_painter.goto(-250,-250)
timmy_the_painter.speed(200)

def draw_line():
    i = 0
    while i < 10:
        timmy_the_painter.pendown()
        timmy_the_painter.dot(20)
        timmy_the_painter.penup()
        timmy_the_painter.forward(50)
        i+=1
a = 0
position = -200
while a < 10:
    draw_line()
    timmy_the_painter.penup()
    timmy_the_painter.goto(-250,position)
    a +=1
    position += 50
screen = Screen()
screen.exitonclick()