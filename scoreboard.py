from turtle import Turtle

import parameters


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(parameters.SCREEN_BOUNDARY_LEFT + parameters.PLAYER_SIZE,
                  parameters.SCREEN_BOUNDARY_TOP - parameters.PLAYER_SIZE * 2)
        self.update_scoreboard()
        self.sleep_time = parameters.CAR_SPEED_START

    def update_scoreboard(self):
        self.write(f'Level: {
                   self.level}', align=parameters.SCORE_ALIGNMENT, font=parameters.SCORE_FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
        self.sleep_time *= parameters.CAR_SPEED_INCREASE

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align=parameters.GAMEOVER_ALIGNMENT,
                   font=parameters.GAMEOVER_FONT)
