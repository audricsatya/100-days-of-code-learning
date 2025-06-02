from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.move_distance = MOVE_DISTANCE
        self.finish_line_y = FINISH_LINE_Y

    def move(self):
        self.forward(self.move_distance)
    
    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)
    
    def is_at_finish_line(self):
        if self.ycor() > self.finish_line_y:
            return True
        return False
