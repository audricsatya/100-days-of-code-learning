from turtle import Turtle

class Ball(Turtle):
    def __init__(self, width, height):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.speed("slow")
        self.x_move = 10
        self.y_move = 10
        self.height = int(height / 2)
        self.width = int(width / 2)
        self.move_speed = 0.05


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # if new_x > (self.width - 20) or new_x < (-self.width + 20):  
        #     self.x_move *= -1
        if new_y > (self.height - 20) or new_y < (-self.height + 20):  
            self.y_move *= -1
        self.goto(new_x, new_y)

    def bounce(self):
        self.x_move *= -1
        # self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce()