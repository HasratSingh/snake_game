from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as text:
            saved_score = text.read()
        self.score = 0
        self.high_score = int(saved_score)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as text:
                text.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game Over! Final Score: {self.score}", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score:{self.high_score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
