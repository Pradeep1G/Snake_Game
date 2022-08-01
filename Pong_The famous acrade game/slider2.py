
from turtle import Turtle, Screen
screen = Screen()


class Slider2(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(6, 1.5)
        self.penup()
        self.speed('fastest')
        self.forward(-700)


    def move_up(self):
        if self.pos()[1]<=300:
            self.goto(self.pos()[0],self.pos()[1]+50)
        screen.update()

    def move_down(self):
        if self.pos()[1]>=-300:
            self.goto(self.pos()[0], self.pos()[1] - 50)
        screen.update()

    def move(self):
        screen.onkey(self.move_up, key="Up")
        screen.onkey(self.move_down, key="Down")


















