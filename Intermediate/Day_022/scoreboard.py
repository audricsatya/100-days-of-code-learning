from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self, height, width):
        super().__init__()
        self.height = int(height/2)
        self.width = int(width/2)
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.align = "center"
        self.update_scoreboard()
        self.penup()
        self.hideturtle()

    def update_scoreboard(self):
        self.goto(0, self.height - 50)
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align=self.align, font=("Courier", 24, "normal"))
    
    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()