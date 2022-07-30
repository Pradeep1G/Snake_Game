from turtle import Turtle, Screen
from snake import Snake
import time, keyboard
from food import Food



screen = Screen()
global is_game_on
is_game_on = True

# time.sleep(0.01)
screen.tracer(0)

scoreBoard = Turtle()

gameOver = Turtle()

def scoreCalci(s):
    scoreBoard.reset()
    sent = "Score : "+str(s)
    scoreBoard.penup()
    scoreBoard.hideturtle()
    scoreBoard.color('White')
    scoreBoard.goto(-10,260)
    scoreBoard.write(sent,False,align = "center",font=("arial",22,"bold"))

def game_over():
    gameOver.penup()
    gameOver.hideturtle()
    gameOver.color("yellow")
    gameOver.write("Game Over",move= False, align= 'center', font = ("arial",48,'bold'))

new_snake = Snake()
food = Food()

screen.update()
# screen.tracer(0)


screen.listen()

screen.onkey(fun = new_snake.move_down , key = 'Down')
screen.onkey(fun = new_snake.move_forward , key = 'Right')
screen.onkey(fun = new_snake.move_backward , key = 'Left')
screen.onkey(fun = new_snake.move_up , key = 'Up')

score = 0
level = 1
scoreCalci((score))

while is_game_on:
    time.sleep(0.25)
    screen.update()
    new_snake.move()
    print(new_snake.snake_head.pos())
    if abs(food.pos()[0] - new_snake.snake_head.pos()[0]) <= 20 and abs(food.pos()[1] - new_snake.snake_head.pos()[1]) <= 20 :
        print(food.pos(),new_snake.snake_head.pos())
        print('Collision occurs')
        score+=1
        scoreCalci(score)
        new_snake.create_bite()
        food.change_position()

    if new_snake.move() == 'Over':
        screen.update()
        game_over()
        break




screen.exitonclick()

