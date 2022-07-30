from turtle import Turtle,Screen
import turtle as t
import random
t.colormode(255)
sha = Turtle()


def rand_col():
    # return (round(random.uniform(0.00,1.00),2),round(random.uniform(0.00,1.00),2),round(random.uniform(0.00,1.00),2))
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

sha.speed(100)

sha.pencolor(rand_col())
def mini_circle():
    sha.circle(1,5)

def max_circle():
    sha.pencolor(rand_col())
    sha.circle(100)

for i in range(75):
    mini_circle()
    max_circle()


screen = Screen()
screen.exitonclick()

