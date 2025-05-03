from turtle import *

bgcolor("black")
color("lime")
speed(0)
left(90)
penup()
goto(0, -250)
pendown()

def tree(branch_length):
    if branch_length > 5:
        forward(branch_length)
        right(20)
        tree(branch_length - 15)
        left(40)
        tree(branch_length - 15)
        right(20)
        backward(branch_length)

tree(100)
done()