from turtle import *
import colorsys

bgcolor("black")
speed(0)
hideturtle()

hue = 0 

num_petals = 36
num_loops = 50

for i in range(num_loops):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pencolor(color)
    hue += 1 / num_loops  
    
    for j in range(num_petals):
        forward(100)
        right(60)
        forward(100)
        right(120)
        forward(100)
        right(60)
        forward(100)
        right(120)
        
        right(360 / num_petals) 

    right(360 / num_loops) 

done()
