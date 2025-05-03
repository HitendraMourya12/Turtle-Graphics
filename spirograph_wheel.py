from turtle import *
import colorsys

bgcolor("black")
speed(0)
hideturtle()

hue = 0
for i in range(72):
    c = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(c)
    hue += 0.014
    circle(100)
    right(5)

done()
