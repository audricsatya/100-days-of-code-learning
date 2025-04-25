from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 1400
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turns off the screen updates

r_paddle = Paddle(WIDTH, HEIGHT, ((WIDTH/2)-50, 0))
l_paddle = Paddle(WIDTH, HEIGHT, ((-WIDTH/2)+50, 0))

ball = Ball(WIDTH, HEIGHT)
scoreboard = Scoreboard(HEIGHT, WIDTH)

screen.update()  # Update the screen to show the initial state

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # Control the speed of the ball
    ball.move()
    screen.update()  # Update the screen to show the current state
    screen.update()  # Final update to show the game over state

    # detect collision with r_paddle
    if ball.xcor() > (WIDTH/2)-70 and ball.distance(r_paddle) < 50:
        ball.bounce()
        ball.move_speed *= 0.9
    # detect collision with l_paddle
    if ball.xcor() < (-WIDTH/2)+70 and ball.distance(l_paddle) < 50:
        ball.bounce()
        ball.move_speed *= 0.9

    # detect miss the ball
    if ball.xcor() > (WIDTH/2)-10 or ball.xcor() < (-WIDTH/2)+10:
        if ball.xcor() > (WIDTH/2)-10:
            scoreboard.increase_l_score()
        else:
            scoreboard.increase_r_score()
        ball.reset_position()
        ball.move_speed = 0.05

screen.exitonclick() 