from turtle import Turtle, Screen
import random

# setting up the variable
color_list = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
y_positions = [-90, -60, -30, 0, 30, 60, 90]
all_turtles = []
width = 1920
height = 400
start = (-width/2) + 20
end = (width/2) - 20

screen = Screen() 
screen.setup(
    width=width, 
    height=height
)

# input for user bet
user_bet = None
while not user_bet:
    user_bet = screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? Enter a color: "
    )

# debugging user
if user_bet:
    user_bet = user_bet.lower()
    if user_bet not in color_list:
        print("Invalid color. Please choose from the list.")
        screen.bye()
    else:  
        print(f"You have bet on {user_bet} turtle.")
        is_race_on = True

# looping turtles
for turtle_number in range(0,len(color_list)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color_list[turtle_number])
    new_turtle.penup()
    new_turtle.goto(start, y_positions[turtle_number])
    all_turtles.append(new_turtle)

while is_race_on: 
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > end:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle wins!")
            else:
                print(f"You lose! The {winning_color} turtle wins!")