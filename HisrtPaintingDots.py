from turtle import Turtle,Screen
import turtle as t
import random
t.colormode(255)
sha = Turtle()

def rand_col():
    # return (round(random.uniform(0.00,1.00),2),round(random.uniform(0.00,1.00),2),round(random.uniform(0.00,1.00),2))
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# t.setposition(-50,-50)
# sha.pendown()
sha.color('white')

sha.setposition(-275,-275)

sha.speed(100)
sha.pensize(25)
def draw_dot():
    sha.pendown()
    print(sha.position)
    sha.color(rand_col())
    sha.circle(1)
    sha.penup()

# sha.speed(1)
draw_dot()

sha.forward(60)

for i in range(1,101):
    if i == 100:
        break
    if (i/10)%2 == 1:
        print(1)
        sha.left(90)
        sha.forward(60)
        sha.left(90)
    elif (i/10)%2 == 0:
        print(0)
        sha.right(90)
        sha.forward(60)
        sha.right(90)
    else:
        if i != 1:
            sha.forward(60)

    draw_dot()




screen = Screen()
screen.exitonclick()


