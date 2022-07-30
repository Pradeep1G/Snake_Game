
from turtle import Turtle, Screen
import time
import keyboard
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("                                                                         Snake Game")
global is_game_on
is_game_on = True


class Snake:

    def __init__(self):
        self.snake_size = 3
        self.bites = []
        self.create_snake()
        self.snake_head = self.bites[0]

    def create_snake(self):
        for i in range(self.snake_size):
            snake_bite = Turtle('circle')
            snake_bite.color('white')
            snake_bite.penup()
            snake_bite.goto(i * (-20), 0)
            snake_bite.speed(0)
            self.bites.append(snake_bite)
        self.bites[0].color("orange")

    def create_bite(self):
        snake_bite = Turtle('circle')
        snake_bite.color('white')
        snake_bite.penup()
        snake_bite.goto(self.bites[self.snake_size-1].pos()[0], self.bites[self.snake_size-1].pos()[1])
        snake_bite.speed(0)
        self.bites.append(snake_bite)
        self.snake_size += 1

    def move(self):
        global is_game_on

        if self.bites[0].pos()[0] >= 290 or self.bites[0].pos()[1] >= 290 or self.bites[0].pos()[0] <= -290 or self.bites[0].pos()[1] <= -290 or \
                self.self_collision(self.snake_head.pos()) == 'Over':
            is_game_on = False
            return 'Over'
        for bite_number in range(len(self.bites) - 1, 0, -1):
            self.bites[bite_number].goto(self.bites[bite_number - 1].pos()[0], self.bites[bite_number - 1].pos()[1])
        self.bites[0].forward(20)

    def move_forward(self):
        if self.bites[0].heading() != 180:
            self.bites[0].setheading(0)
            self.move()

    def move_backward(self):
        if self.bites[0].heading() != 0:
            self.bites[0].setheading(180)
            self.move()

    def move_up(self):
        if self.bites[0].heading() != 270:
            self.bites[0].setheading(90)
            self.move()

    def move_down(self):
        if self.bites[0].heading() != 90:
            self.bites[0].setheading(270)
            self.move()

    def self_collision(self,snake_pos):
        for bite in self.bites:
            if abs(snake_pos[1] - bite.pos()[1]) <=15 and abs(snake_pos[0] - bite.pos()[0]) <=15 and self.snake_head.heading() != bite.heading():
                bite.color('red')
                self.snake_head.color('red')
                return "Over"





   # def move_forward(self):
    #     time.sleep(0.1)
    #     screen.update()
    #     global is_game_on
    #
    #     current_head = self.bites[0].heading()
    #     if current_head != 180 and is_game_on:
    #         for i, bite in enumerate(self.bites):
    #             if keyboard.is_pressed('Up') or keyboard.is_pressed('Down') or keyboard.is_pressed('Left'):
    #                 return
    #             # if i == 1:
    #             #     time.sleep(0.1)
    #             # else:
    #             #     time.sleep(0.001)
    #             time.sleep(0.1)
    #             screen.update()
    #             if self.bites[i].heading() != 0:
    #                 bite.setheading(0)
    #             for bite in self.bites:
    #                 if keyboard.is_pressed('Up') or keyboard.is_pressed('Down') or keyboard.is_pressed('Left'):
    #                     return
    #                 bite.forward(20)
    #
    #         while is_game_on:
    #             time.sleep(0.1)
    #             screen.update()
    #             if self.bites[0].pos()[0] >= 270:
    #                 is_game_on = False
    #                 break
    #             for bite_number in range(len(self.bites) - 1, 0, -1):
    #                 self.bites[bite_number].goto(self.bites[bite_number - 1].pos()[0], self.bites[bite_number - 1].pos()[1])
    #             self.bites[0].forward(20)

    # def move_backward(self):
    #     time.sleep(0.1)
    #     screen.update()
    #     global is_game_on
    #
    #     current_head = self.bites[0].heading()
    #     if current_head != 0 and is_game_on:
    #         for i, bite in enumerate(self.bites):
    #             if keyboard.is_pressed('Up') or keyboard.is_pressed('Down') or keyboard.is_pressed('Right'):
    #                 return
    #             time.sleep(0.1)
    #             screen.update()
    #             if self.bites[i].heading() != 180:
    #                 bite.setheading(180)
    #
    #             for bite in self.bites:
    #                 if keyboard.is_pressed('Up') or keyboard.is_pressed('Down') or keyboard.is_pressed('Right'):
    #                     return
    #                 bite.forward(20)
    #
    #         while is_game_on:
    #             time.sleep(0.1)
    #             screen.update()
    #             if self.bites[0].pos()[0] <= -280:
    #                 is_game_on = False
    #                 break
    #             for bite_number in range(len(self.bites) - 1, 0, -1):
    #                 self.bites[bite_number].goto(self.bites[bite_number - 1].pos()[0], self.bites[bite_number - 1].pos()[1])
    #             self.bites[0].forward(20)

    # def move_down(self):
    #     time.sleep(0.1)
    #     screen.update()
    #     global is_game_on
    #     current_head = self.bites[0].heading()
    #     if current_head != 90 and is_game_on:
    #         for i, bite in enumerate(self.bites):
    #             if keyboard.is_pressed('Up') or keyboard.is_pressed('Right') or keyboard.is_pressed('Left'):
    #                 return
    #             time.sleep(0.1)
    #             screen.update()
    #             if self.bites[i].heading() != 270:
    #                 bite.setheading(270)
    #             for bite in self.bites:
    #                 if keyboard.is_pressed('Up') or keyboard.is_pressed('Right') or keyboard.is_pressed('Left'):
    #                     return
    #                 bite.forward(20)
    #
    #         while is_game_on:
    #             time.sleep(0.1)
    #             screen.update()
    #             if self.bites[0].pos()[1] <= -270:
    #                 is_game_on = False
    #                 break
    #             for bite_number in range(len(self.bites) - 1, 0, -1):
    #                 self.bites[bite_number].goto(self.bites[bite_number - 1].pos()[0], self.bites[bite_number - 1].pos()[1])
    #             self.bites[0].forward(20)

    # def move_up(self):
    #     print("hiii")
    #     time.sleep(0.1)
    #     screen.update()
    #     global is_game_on
    #     current_head = self.bites[0].heading()
    #     if current_head != 270 and is_game_on:
    #         for i, bite in enumerate(self.bites):
    #             if keyboard.is_pressed('Down') or keyboard.is_pressed('Right') or keyboard.is_pressed('Left'):
    #                 return
    #             time.sleep(0.1)
    #             screen.update()
    #             if self.bites[i].heading() != 90:
    #                 bite.setheading(90)
    #             for bite in self.bites:
    #                 if keyboard.is_pressed('Down') or keyboard.is_pressed('Right') or keyboard.is_pressed('Left'):
    #                     return
    #                 bite.forward(20)
    #
    #         while is_game_on:
    #             time.sleep(0.1)
    #             screen.update()
    #             if self.bites[0].pos()[1] >= 270:
    #                 is_game_on = False
    #                 break
    #             for bite_number in range(len(self.bites) - 1, 0, -1):
    #                 self.bites[bite_number].goto(self.bites[bite_number - 1].pos()[0], self.bites[bite_number - 1].pos()[1])
    #             self.bites[0].forward(20)