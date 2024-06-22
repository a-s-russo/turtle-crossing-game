import time
from turtle import Screen, Turtle

import car
import parameters
import player
import scoreboard

screen = Screen()
screen.setup(width=parameters.WIDTH, height=parameters.HEIGHT)
screen.bgcolor('grey')
screen.title('Turtle Crossing')
screen.tracer(0)

# Create bottom road line
centre_line = Turtle()
centre_line.pensize(parameters.ROAD_LINE_THICKNESS)
centre_line.hideturtle()
centre_line.color('white')
centre_line.penup()
centre_line.teleport(parameters.SCREEN_BOUNDARY_LEFT -
                     parameters.PLAYER_SIZE * 2, parameters.PLAY_BOUNDARY_BOTTOM)
centre_line.setheading(0)

# Print bottom road line
for _ in range(int(parameters.WIDTH)):
    centre_line.forward(parameters.PLAYER_SIZE)
    centre_line.penup()
    centre_line.forward(parameters.PLAYER_SIZE)
    centre_line.pendown()

# Create top road line
centre_line = Turtle()
centre_line.pensize(parameters.ROAD_LINE_THICKNESS)
centre_line.hideturtle()
centre_line.color('white')
centre_line.penup()
centre_line.teleport(parameters.SCREEN_BOUNDARY_LEFT - parameters.PLAYER_SIZE * 2,
                     parameters.PLAY_BOUNDARY_TOP + parameters.PLAYER_SIZE / 2)
centre_line.setheading(0)

# Print top road line
for _ in range(int(parameters.WIDTH)):
    centre_line.forward(parameters.PLAYER_SIZE)
    centre_line.penup()
    centre_line.forward(parameters.PLAYER_SIZE)
    centre_line.pendown()

# Create player
player = player.Player()

# Create key bindings for player
screen.listen()
screen.onkey(player.up, 'Up')

# Create scoreboard
scoreboard = scoreboard.Scoreboard()

# Generate starting cars
cars = []
for _ in range(parameters.CAR_STARTING_NUMBER):
    new_car = car.Car()
    cars.append(new_car)

# Simulate game
game_is_on = True
while game_is_on:
    time.sleep(scoreboard.sleep_time)
    screen.update()

    # Move cars
    for car in cars:
        car.move()

        # Detect collision
        if car.distance(player) <= parameters.PLAYER_SIZE:
            game_is_on = False
            scoreboard.game_over()

        if car.xcor() <= parameters.SCREEN_BOUNDARY_LEFT - parameters.CAR_DISTANCE_ENDING:
            car.restart()

    # Reach other side
    if player.ycor() > parameters.PLAY_BOUNDARY_TOP:
        player.restart()
        scoreboard.increase_level()

screen.exitonclick()
