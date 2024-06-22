from random import choice, randint
from turtle import Turtle

import parameters


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=parameters.CAR_SIZE, stretch_wid=1)
        self.restart()

    def restart(self):
        self.color(choice(parameters.CAR_COLOURS))
        self.goto(
            parameters.SCREEN_BOUNDARY_RIGHT + parameters.PLAYER_SIZE *
            randint(1, parameters.CAR_DISTANCE_STARTING),
            randint(int(parameters.PLAY_BOUNDARY_BOTTOM + parameters.PLAYER_SIZE / 2),
                    int(parameters.PLAY_BOUNDARY_TOP)))

    def move(self):
        new_x = self.xcor() - parameters.CAR_MOVEMENT_STEP
        self.goto(new_x, self.ycor())
