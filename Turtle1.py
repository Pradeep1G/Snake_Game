from turtle import Turtle,Screen
import turtle as t
import random
t.colormode(255)
sha = Turtle()

li = [3,4,5,6,7,8]
colours = ['red', 'green', 'blue', 'pink', 'violet', 'yellow']
angle = [0,90,180,270]

def rand_col():
    # return (round(random.uniform(0.00,1.00),2),round(random.uniform(0.00,1.00),2),round(random.uniform(0.00,1.00),2))
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

# print(rand_col())
sha.pensize(10)
sha.speed(100)
for i in range(500):
    sha.pencolor(rand_col())
    sha.forward(25)
    sha.right(random.choice(angle))
    # sha.right(270)





# def draw():
#     for c,i in enumerate(li):
#         for j in range(i):
#             sha.speed(50)
#             sha.color(colours[c])
#             sha.forward(100)
#             sha.right(360/i)
# draw()


# def square():
#     sha.color('red')
#     sha.forward(100)
#     sha.right(90)
#     sha.forward(100)
#     sha.right(90)
#     sha.forward(100)
#     sha.right(90)
#     sha.forward(100)
#     sha.right(90)
#
# def triangle():
#     sha.color('green')
#     sha.forward(100)
#     sha.right(120)
#     sha.forward(100)
#     sha.right(120)
#     sha.forward(100)
#     sha.right(120)
#
# def pentagon():
#     sha.color('yellow')
#     sha.forward(100)
#     sha.right(72)
#     sha.forward(100)
#     sha.right(72)
#     sha.forward(100)
#     sha.right(72)
#     sha.forward(100)
#     sha.right(72)
#     sha.forward(100)
#     sha.right(72)
#
# def hexagon():
#     sha.color('blue')
#     sha.forward(100)
#     sha.right(60)
#     sha.forward(100)
#     sha.right(60)
#     sha.forward(100)
#     sha.right(60)
#     sha.forward(100)
#     sha.right(60)
#     sha.forward(100)
#     sha.right(60)
#     sha.forward(100)
#     sha.right(60)
#
# def heptagon():
#     sha.color('pink')
#     sha.forward(100)
#     sha.right(360/7)
#     sha.forward(100)
#     sha.right(360/7)
#     sha.forward(100)
#     sha.right(360/7)
#     sha.forward(100)
#     sha.right(360/7)
#     sha.forward(100)
#     sha.right(360/7)
#     sha.forward(100)
#     sha.right(360/7)
#     sha.forward(100)
#     sha.right(360/7)
#
# def octagon():
#     sha.color('orange')
#     sha.forward(100)
#     sha.right(360 / 8)
#     sha.forward(100)
#     sha.right(360 / 8)
#     sha.forward(100)
#     sha.right(360 / 8)
#     sha.forward(100)
#     sha.right(360 / 8)
#     sha.forward(100)
#     sha.right(360 / 8)
#     sha.forward(100)
#     sha.right(360 / 8)
#     sha.forward(100)
#     sha.right(360 / 8)
#     sha.forward(100)
#     sha.right(360 / 8)
#
#
# triangle()
# square()
# pentagon()
# hexagon()
# heptagon()
# octagon()
#
#
#
#
#




screen = Screen()
screen.exitonclick()

