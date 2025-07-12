from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600) 
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # Turns off the screen updates

segments = []
for i in range(3):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(-20 * i, 0)
    segments.append(new_segment)

game_is_on = True
loop = 0

while game_is_on:
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    loop += 1
    print(loop)
    if loop == 4:
        loop = 0
        segments[0].left(90)  # Change direction to up
        segments[0].forward(20)  # Move forward after turning
    screen.update()
    time.sleep(0.1)


screen.exitonclick()