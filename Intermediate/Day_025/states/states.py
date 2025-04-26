import turtle
import pandas as pd

# Set up the screen
screen = turtle.Screen()
screen.title("State Game")
image = "Intermediate/Day_025/states/blank_states_img.gif"
states_file = "Intermediate/Day_025/states/50_states.csv"
screen.addshape(image)
turtle.shape(image)

# Load state data
states_location = pd.read_csv(states_file)
all_states = states_location["state"].to_list()
guessed_states = []
correct_guesses = 0

# Create a new turtle for writing text
text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

# Main game loop
while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f"{correct_guesses}/50 States Correct",
        prompt="What's another state's name? (Type 'exit' to give up)"
    )
    if not answer:
        continue
    answer = answer.title()

    if answer == "Exit":
        # Save missing states to a file
        missing_states = [state for state in all_states if state not in guessed_states]
        print(missing_states)
        pd.DataFrame(missing_states).to_csv("Intermediate/Day_025/states/states_to_learn.csv", index=False)
        print("Missing states saved to 'states_to_learn.csv'.")
        break

    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        correct_guesses += 1
        state_data = states_location[states_location["state"] == answer]
        x = int(state_data["x"])
        y = int(state_data["y"])
        text_turtle.goto(x, y)
        text_turtle.write(answer, align="center", font=("Arial", 8, "normal"))
    else:
        print("Incorrect or already guessed. Try again.")
