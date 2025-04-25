from turtle import Turtle

FILE_LOCATION = 'intermediate/Day_024/Snake/score.txt'

with open(FILE_LOCATION) as f:
    highscore = f.read()

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self, height, width):
        super().__init__()
        self.height = int(height/2)
        self.width = int(width/2)
        self.score = 0
        try:
            self.highscore = int(highscore)
        except:
            self.highscore = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, self.height - 60)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, self.height - 60)
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(FILE_LOCATION, 'w') as f:
                f.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)