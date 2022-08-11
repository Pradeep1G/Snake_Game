import time
from turtle import Turtle, Screen
from cars import Cars


screen = Screen()
screen.setup(width=500, height=500)
screen.tracer(0)
screen.listen()

tom = Turtle('turtle')
tom.penup()
tom.setheading(90)
tom.goto(0,-210)

def move_tom():
    tom.forward(10)


car1 = Cars()


screen.onkey(move_tom, key = 'Up')

is_game_on = True

while is_game_on:
    car1.row1()
    screen.update()
    time.sleep(0.1)
    car1.row1_move()
    print(len(car1.cars))






screen.exitonclick()


