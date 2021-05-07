from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! Final Score: {self.score}", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
