from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, height, width):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.height = int(height/2)
        self.width = int(width/2)
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-(self.height) + 20, (self.height) - 20)
        y = random.randint(-(self.width) + 20, (self.width) - 20)
        self.goto(x, y)