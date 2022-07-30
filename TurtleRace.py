from turtle import Turtle,Screen
import turtle as t
import random
t.colormode(255)

screen = Screen()
player_turtle = screen.textinput(title='Make your bet', prompt="What is your turtle color? : ")

tom1 = Turtle()
tom1.hideturtle()
tom1.speed("fastest")
tom1.shape('turtle')
tom1.penup()
tom1.setposition(-300,-200)
tom1.color('pink')
tom1.showturtle()


tom2 = Turtle()
tom2.hideturtle()
tom2.speed("fastest")
tom2.shape('turtle')
tom2.penup()
tom2.setposition(-300,-100)
tom2.color('blue')
tom2.showturtle()

tom3 = Turtle()
tom3.hideturtle()
tom3.speed("fastest")
tom3.shape('turtle')
tom3.penup()
tom3.setposition(-300,0)
tom3.color('green')
tom3.showturtle()

tom4 = Turtle()
tom4.hideturtle()
tom4.speed("fastest")
tom4.shape('turtle')
tom4.penup()
tom4.setposition(-300,100)
tom4.color('yellow')
tom4.showturtle()

tom5 = Turtle()
tom5.hideturtle()
tom5.speed("fastest")
tom5.shape('turtle')
tom5.penup()
tom5.setposition(-300,200)
tom5.color('red')
tom5.showturtle()

win_line = Turtle()
win_line.hideturtle()
win_line.speed('fastest')
win_line.penup()
win_line.setposition(300,220)
win_line.pendown()
win_line.pensize(10)
win_line.right(90)
win_line.pencolor('green')
win_line.forward(440)
win_line.showturtle()


def race():
    tom1.forward(random.randint(1,5))
    tom2.forward(random.randint(1,5))
    tom3.forward(random.randint(1,5))
    tom4.forward(random.randint(1,5))
    tom5.forward(random.randint(1,5))

for i in range(400):
    race()
    # print(tom1.pos())
    if tom1.pos()[0] >= 300 or tom2.pos()[0] >= 300 or tom3.pos()[0] >= 300 or tom4.pos()[0] >= 300 or tom5.pos()[0] >= 300:
        if tom1.pos()[0] > tom2.pos()[0] and tom1.pos()[0]>tom3.pos()[0] and tom1.pos()[0]>tom4.pos()[0] and tom1.pos()[0]>tom5.pos()[0]:
            if player_turtle.lower() == 'pink':
                print("You win. The pink turtle is the winner.")
            else:
                print('You lose. The pink turtle is the winner.')
            break
        if tom2.pos()[0] > tom1.pos()[0] and tom2.pos()[0] > tom3.pos()[0] and tom2.pos()[0] > tom4.pos()[0] and tom2.pos()[0] > tom5.pos()[0]:
            if player_turtle.lower() == 'blue':
                print("You win. The blue turtle is the winner.")
            else:
                print('You lose. The blue turtle is the winner.')
            break
        if tom3.pos()[0] > tom1.pos()[0] and tom3.pos()[0]>tom2.pos()[0] and tom3.pos()[0]>tom4.pos()[0] and tom3.pos()[0]>tom5.pos()[0]:
            if player_turtle.lower() == 'green':
                print("You win. The green turtle is the winner.")
            else:
                print('You lose. The green turtle is the winner.')
            break
        if tom4.pos()[0] > tom1.pos()[0] and tom4.pos()[0]>tom2.pos()[0] and tom4.pos()[0]>tom3.pos()[0] and tom4.pos()[0]>tom5.pos()[0]:
            if player_turtle.lower() == 'yellow':
                print("You win. The yellow turtle is the winner.")
            else:
                print('You lose. The yellow turtle is the winner.')
            break
        if tom5.pos()[0] > tom1.pos()[0] and tom5.pos()[0]>tom2.pos()[0] and tom5.pos()[0]>tom3.pos()[0] and tom5.pos()[0]>tom4.pos()[0]:
            if player_turtle.lower() == 'red':
                print("You win. The red turtle is the winner.")
            else:
                print('You lose. The red turtle is the winner.')
            break


# tom6 = Turtle()
# tom7 = Turtle()
# tom8 = Turtle()
# tom9 = Turtle()
# tom10 = Turtle()









screen.exitonclick()

