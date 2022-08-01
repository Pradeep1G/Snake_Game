

from turtle import Turtle, Screen
from slider1 import Slider1
from slider2 import Slider2
from ball import Ball
import random
import time

screen = Screen()
screen.setup(width = 1600, height = 800)
screen.bgcolor('black')

right = [x for x in range(0,30)] + [x for x in range(330,359)]
left = [x for x in range(150,210)]
angle = random.choice(right)

def middle_line(y_cor):
    line = Turtle()
    line.color('white')
    line.shape("square")
    line.shapesize(1.5,0.4)
    line.penup()
    line.goto(0,y_cor)

screen.tracer(0)

scoreboard = Turtle()

def score_update(score1,score2):
    scoreboard.reset()
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.color('white')
    scoreboard.goto(-10,320)
    scoreboard.write(f"{score2}           {score1}", False, align = "center", font=("arial", 48, "bold"))

def winner(person):
    # scoreboard.reset()
    scoreboard.hideturtle()
    scoreboard.penup()
    scoreboard.color('white')
    scoreboard.goto(-10,0)
    scoreboard.write(f"{person}  is win🏆", False, align = "center", font=("arial", 48, "bold"))




player1 = Slider1()
player2 = Slider2()
ball1 = Ball(angle)

for i in range(-6,7):
    middle_line(i*60)
screen.update()

is_game_on = True
plr1_chance = True
plr2_chance = True
screen.listen()

plr1_score = 0
plr2_score = 0

score_update(plr1_score,plr2_score)

# target = int(screen.textinput("Target Score","Challenge Score (enter a number)"))
target = 6

while is_game_on:
    # time.sleep(0.1)
    # screen.update()

    while plr1_chance:
        time.sleep(0.001)
        # print('hi')
        ball1.start_move()

        player1.move()
        print(player1.pos()[0],ball1.pos()[0])

        if player1.pos()[0] - ball1.pos()[0] <= 30 and abs(player1.pos()[1] - ball1.pos()[1]) <= 50:
            print(player1.pos(),ball1.pos(),"       ",player1.distance(ball1))
        # if player1.distance(ball1) <= 20:
            print(player1.pos()[0] - ball1.pos()[0] <= 30)
            print(player1.pos()[0] - ball1.pos()[0] <= 30)
            ball1.angle = random.choice(left)
            print("       ",ball1.angle)
            plr1_chance = False
            plr2_chance = True

        if ball1.pos()[0]>890 or ball1.pos()[0]<-890:
            plr2_score += 1
            score_update(plr1_score,plr2_score)
            if target == plr2_score:
                winner("Player2👈")
                plr1_chance = False
                plr2_chance = False
                is_game_on = False
                break
            # ball1.reset()
            ball1.goto(0,0)
            ball1.angle = random.choice(right)
            plr1_chance = True

    while plr2_chance:
        time.sleep(0.001)
        # print('hi')
        ball1.start_move()

        player2.move()
        print(player2.pos()[0], ball1.pos()[0])

        # if player2.pos()[0] - ball1.pos()[0] >= -30:
        if abs(player2.pos()[0] - ball1.pos()[0]) <= 30 and abs(player2.pos()[1] - ball1.pos()[1]) <= 50:
            ball1.angle = random.choice(right)
            print(ball1.angle)
            plr1_chance = True
            plr2_chance = False

        if ball1.pos()[0]>890 or ball1.pos()[0]<-890:
            plr1_score += 1
            score_update(plr1_score,plr2_score)
            if target == plr1_score:
                winner("Player1👉")
                plr1_chance = False
                plr2_chance = False
                is_game_on = False
                break
            # ball1.reset()
            ball1.goto(0,0)
            ball1.angle = random.choice(right)
            plr1_chance = True
            break





screen.exitonclick()