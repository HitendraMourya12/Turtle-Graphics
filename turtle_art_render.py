from turtle import *

bgcolor("black")
color("white")
penup()
goto(-200, 100)
hideturtle()
speed(0)

lines = [
    "The moon sleeps in a glass of ink,",
    "Wind hums a song of scattered stars,",
    "Time pirouettes on broken clocks,",
    "And silence paints the dark with scars."
]

for i, line in enumerate(lines):
    write(line, font=("Courier", 16, "normal"))
    goto(-200, 100 - (i + 1) * 40)
    # Draw a swirl or shape after each line
    pendown()
    color("cyan")
    circle(30 + i * 10, 180)
    penup()

done()