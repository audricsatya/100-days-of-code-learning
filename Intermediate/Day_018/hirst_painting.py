import colorgram

# Extract 30 colors from an image and print their RGB values
# Note: You need to have the image 'image.jpg' in the same directory as this script.
rgb_color = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    print(color.rgb)
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_color.append(new_color)

rgb_color = [
    (33, 30, 28), (86, 96, 104), (40, 42, 48), (143, 160, 173), (207, 216, 224),
    (89, 87, 82), (97, 102, 100), (36, 34, 36), (232, 231, 228), (163, 160, 152),
    (41, 44, 42), (150, 156, 154), (220, 224, 222), (57, 62, 73), (231, 228, 230), 
    (109, 129, 149), (83, 79, 81), (177, 193, 207), (67, 65, 56), (162, 158, 160), 
    (117, 131, 136), (132, 131, 116), (122, 131, 128), (196, 194, 181), (178, 195, 203), 
    (68, 62, 60), (57, 66, 69), (59, 66, 63), (66, 62, 64), (186, 195, 191)]

import turtle
import random

# Set up the turtle screen
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

vertical_dots = 10
horizontal_dots = 10

for y in range(vertical_dots):
    for x in range(horizontal_dots):
        timmy.dot(20, random.choice(rgb_color))
        timmy.forward(50)
    timmy.backward(500)
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()