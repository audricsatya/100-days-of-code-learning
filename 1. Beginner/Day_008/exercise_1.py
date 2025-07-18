# Write your code below this line 👇
import math

def paint_calc(height, width, cover):
    no_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {no_of_cans} cans of paint.")

# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
try:
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5

    paint_calc(height=test_h, width=test_w, cover=coverage)
except ValueError:
    print("Please enter valid integer values for height and width.")