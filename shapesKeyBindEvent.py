from turtle import Turtle,Screen
import turtle as t
import random
t.colormode(255)
sha = Turtle()
screen = Screen()


def clear_screen():
    sha.penup()
    sha.clear()
    sha.home()
    sha.pendown()

def move_forward():
    sha.forward(50)

def move_backward():
    sha.back(50)

def turn_around_anti_clockwisw():
    sha.setheading(sha.heading()+1)

def turn_around_clockwise():
    sha.setheading(sha.heading()-1)

screen.onkey(fun = move_forward, key = 'w')
screen.onkey(fun = move_backward, key = 's')
screen.onkeypress(fun = turn_around_anti_clockwisw, key = 'a')
screen.onkeypress(fun = turn_around_clockwise, key = 'c')
screen.onkey(fun = clear_screen, key = 'd')
screen.listen()












screen.exitonclick()

