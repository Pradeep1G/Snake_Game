from turtle import Turtle,Screen
import turtle as t
import random
t.colormode(255)
sha = Turtle()

# sha.pensize(50)
sha.hideturtle()
sha.fillcolor('yellow')
sha.begin_fill()
sha.shape()
sha.speed('fastest')
def square():
    for i in range(4):
        sha.forward(25)
        sha.right(90)

square()
sha.end_fill()



screen = Screen()
screen.exitonclick()

