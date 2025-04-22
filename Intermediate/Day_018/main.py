from turtle import Turtle, Screen
import random

# This is a simple turtle graphics program that creates various shapes and patterns using the turtle module in Python.

timmy = Turtle()
timmy.shape("turtle")
timmy.color("silver")
timmy.pensize(10)
timmy.forward(100)
timmy.right(90)

color_list = ["red", "blue", "green", "yellow", "purple", "orange"]
directions = [0, 90, 180, 270]

# Create Square
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

# Create Triangle
for _ in range(3):
    timmy.forward(100)
    timmy.right(120)

# Create dashed line
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

# Create Difference Shapes
timmy.speed("fastest") 
for angle in range(3, 360):
    timmy.color(random.choice(color_list))
    for _ in range(angle):
        timmy.forward(10)
        timmy.right(360 / angle)

# Generated random color
screen = Screen()
screen.colormode(255)  # Set color mode to 255 for RGB values

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
random_number = lambda: random.randint(0, 255)
timmy.color(random_number(), random_number(), random_number())

# Random Movement
for _ in range(100):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))

# Create a spirograph
timmy.speed("fastest")
for angle in range(0, 360, 10):
    timmy.color(random_color())
    timmy.circle(10)
    timmy.setheading(angle)

screen = Screen()
screen.exitonclick() 
