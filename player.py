from turtle import Turtle

import parameters


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(parameters.PLAYER_START_HEADING)
        self.restart()

    def restart(self):
        self.goto(0, parameters.PLAY_BOUNDARY_BOTTOM - parameters.PLAYER_SIZE)

    def up(self):
        new_y = self.ycor() + parameters.PLAYER_MOVEMENT_STEP
        self.goto(self.xcor(), new_y)
