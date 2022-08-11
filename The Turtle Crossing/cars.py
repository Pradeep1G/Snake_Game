

from turtle import Turtle, Screen
import random
import time

screen = Screen()
screen.tracer(0)

global is_game_on
is_game_on = True

class Cars:

    def __init__(self):
        self.cars = []
        self.carsizes = [1.5,2,2.5]
        self.position = 240
        self.gaps = [100, 50, 80, 60, 120]

        # self.row1()

    def row1_move(self):
        for item in self.cars:
            # time.sleep(0.05)
            screen.update()
            item.forward(30)

    def row1(self):
        global is_game_on
        # time.sleep(0.5)
        # screen.update()
        self.car = Turtle()
        self.car.shape('square')
        self.car.penup()
        self.car.setheading(180)
        self.car.goto(self.position, -170)
        self.position += random.choice(self.gaps)
        self.car.shapesize(1,random.choice(self.carsizes))
        self.cars.append(self.car)
        # self.row1_move()



