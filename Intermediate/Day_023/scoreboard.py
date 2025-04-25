from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, height, width):
        super().__init__()
        self.height = int(height / 2)
        self.width = int(width / 2)
        self.score = 0
        self.color("black")
        self.align = "center"
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.score += 1
        self.clear()
        self.goto(-self.width + 100, self.height - 50)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def draw_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)

