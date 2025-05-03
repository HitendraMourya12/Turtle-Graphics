from turtle import *
import colorsys

bgcolor("black")
speed(0)
hideturtle()

hue = 0
for i in range(100):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(color)
    hue += 0.01
    for _ in range(6): 
        forward(100 - i)
        right(60)
    right(10)

done()