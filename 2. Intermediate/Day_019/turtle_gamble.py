import turtle

# Create a turtle object
timmy = turtle.Turtle()
screen = turtle.Screen()
screen.title("Manual Turtle Control")

# Set the speed of the turtle
timmy.speed(1)

def move_forward():
    timmy.forward(10)

def move_backward():
    timmy.backward(10)

def turn_left():
    timmy.left(10)

def turn_right():
    timmy.right(10)

def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear_screen, "Space")

screen.exitonclick()