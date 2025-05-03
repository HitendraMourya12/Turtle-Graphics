from turtle import *
import colorsys

bgcolor("black")
speed(0)
hideturtle()

h = 0
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.005
    forward(i * 0.5)
    left(59)
    circle(i * 0.1, 120)

done()