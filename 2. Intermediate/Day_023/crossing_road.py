import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600
TIME = 0.1

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.title("Turtle Crossing")

# Create player, car manager, and scoreboard instances
player = Player()
car_manager = CarManager(WIDTH, HEIGHT)
scoreboard = Scoreboard(HEIGHT, WIDTH)

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(TIME)  # Control the speed of the cars
    screen.update()  # Update the screen to show the current state

    car_manager.create_car()
    car_manager.move_cars()

    # Check for collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.draw_game_over()
            
    # Check if player has reached the finish line
    if player.ycor() > (HEIGHT / 2) - 10:
        player.reset_position()
        car_manager.level_up()
        scoreboard.update_scoreboard()

    time.sleep(0.1)
    screen.update()
