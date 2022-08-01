

from turtle import Turtle, Screen
screen = Screen()
import random, time

class Ball(Turtle):

    def __init__(self,angle):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.speed('slow')
        self.angle = angle


    def start_move(self):
        time.sleep(0.1)

        self.setheading(self.angle)
        self.forward(30)
        self.setheading(0)
        screen.update()
        if self.pos()[1]>=370 or self.pos()[1]<=-370:
            self.angle = 360-self.angle
            # self.color('red')
            # self.write("i am crossed")
            # print("i am crossed")

        # if self.pos()[1] == -390:


