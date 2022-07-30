import time
from turtle import Turtle, Screen
import random
import turtle as t
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Snake Game")

bites = []
screen.tracer(0)
for i in range(5):
    snake_bite = Turtle('circle')
    snake_bite.color('white')
    snake_bite.penup()
    snake_bite.goto(i*(-20),0)
    snake_bite.speed(0)
    bites.append(snake_bite)
bites[0].color("orange")
screen.update()
screen.tracer(0)

global is_game_on
is_game_on = True

def move_forward():
    global is_game_on

    current_head = bites[0].heading()
    if current_head != 180 and is_game_on:
        for i,bite in enumerate(bites):
            # if i == 1:
            #     time.sleep(0.1)
            # else:
            #     time.sleep(0.001)
            time.sleep(0.1)
            screen.update()
            if bites[i].heading() != 0:
                print('hi')
                bite.setheading(0)
            for bite in bites:
                bite.forward(20)

        while is_game_on:
            time.sleep(0.1)
            screen.update()
            if bites[0].pos()[0]>=270:
                is_game_on = False
                break
            for bite_number in range(len(bites)-1,0,-1):
                bites[bite_number].goto(bites[bite_number-1].pos()[0], bites[bite_number-1].pos()[1])
            bites[0].forward(20)

def move_backward():
    global is_game_on

    current_head = bites[0].heading()
    if current_head != 0 and is_game_on:
        for i,bite in enumerate(bites):
            time.sleep(0.1)
            screen.update()
            if bites[i].heading() != 180:
                print('hi')
                bite.setheading(180)

            for bite in bites:
                bite.forward(20)

        while is_game_on:
            time.sleep(0.1)
            screen.update()
            if bites[0].pos()[0]<=-280:
                is_game_on = False
                break
            for bite_number in range(len(bites)-1,0,-1):
                bites[bite_number].goto(bites[bite_number-1].pos()[0], bites[bite_number-1].pos()[1])
            bites[0].forward(20)


def move_down():
    global is_game_on
    current_head = bites[0].heading()
    if current_head != 90 and is_game_on:
        for i,bite in enumerate(bites):
            time.sleep(0.1)
            screen.update()
            if bites[i].heading() != 270:
                print('hi')
                bite.setheading(270)
            for bite in bites:
                bite.forward(20)

        while is_game_on:
            time.sleep(0.1)
            screen.update()
            if bites[0].pos()[1]<=-270:
                is_game_on = False
                break
            for bite_number in range(len(bites) - 1, 0, -1):
                bites[bite_number].goto(bites[bite_number - 1].pos()[0], bites[bite_number - 1].pos()[1])
            bites[0].forward(20)


def move_up():
    global is_game_on
    current_head = bites[0].heading()
    if current_head != 270 and is_game_on:
        for i,bite in enumerate(bites):
            time.sleep(0.1)
            screen.update()
            if bites[i].heading() != 90:
                bite.setheading(90)
            for bite in bites:
                bite.forward(20)

        while is_game_on:
            time.sleep(0.1)
            screen.update()
            if bites[0].pos()[1]>=270:
                is_game_on = False
                break
            for bite_number in range(len(bites)-1,0,-1):
                bites[bite_number].goto(bites[bite_number-1].pos()[0], bites[bite_number-1].pos()[1])
            bites[0].forward(20)



screen.onkey(fun = move_up, key = 'Up')
screen.onkey(fun = move_down , key = 'Down')
screen.onkey(fun = move_forward , key = 'Right')
screen.onkey(fun = move_backward , key = 'Left')
screen.listen()

screen.exitonclick()

