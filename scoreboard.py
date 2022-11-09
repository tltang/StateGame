from turtle import Turtle
import random

ALIGNMENT = "Center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.speed("fastest")
        self.score_total = -1
        self.high_score = 0
        self.goto(0, 280)
        self.hideturtle()
        self.score()

    def score(self):
        self.score_total += 1
        self.clear()
        self.write(f"Scores: {self.score_total} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=('Arial', 8, 'bold'))

    def reset(self):
        if self.score_total > self.high_score:
            self.high_score = self.score_total

        self.score_total = 0
        self.clear()
        self.write(f"Scores: {self.score_total} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=('Arial', 8, 'bold'))
        with open("data/highscore.txt", mode="w") as f:
            f.write(f"{self.high_score}")

    def game_over(self, reason):
        if reason == 1:
            display_text = "GAME OVER! Hit the wall."
        else:
            display_text = "GAME OVER! Hit the tail."
        self.color("red")
        self.home()
        self.write(display_text, move=False, align="center", font=('Arial', 12, 'bold'))

    def retr_highscore(self):
        with open("data/highscore.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.clear()
        self.write(f"Scores: {self.score_total} High Score: {self.high_score}", move=False, align=ALIGNMENT,
                   font=('Arial', 8, 'bold'))
