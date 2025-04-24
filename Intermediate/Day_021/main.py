from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600
MOVE_DISTANCE = 20

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT) 
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates

snake = Snake()
food = Food(HEIGHT, WIDTH)
scoreboard = Scoreboard(HEIGHT, WIDTH)
screen.update()  # Update the screen to show the initial state

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    time.sleep(0.1)

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if (snake.head.xcor() > int((WIDTH/2)-10) or snake.head.xcor() < int((-WIDTH/2)+10) or
        snake.head.ycor() > int((HEIGHT/2)-10) or snake.head.ycor() < int((-HEIGHT/2)+10)):
        game_is_on = False
        scoreboard.game_over()

    if len(snake.segments) > 1:
        for segment in snake.segments[1:]:
            # if snake.head == segment:
            #     continue
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

screen.update()  # Final update to show the game over state

screen.exitonclick()