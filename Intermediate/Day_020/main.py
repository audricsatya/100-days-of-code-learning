from turtle import Turtle, Screen

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
while game_is_on:
    for segment in segments:
        segment.forward(20)

screen.exitonclick()