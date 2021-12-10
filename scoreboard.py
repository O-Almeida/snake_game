from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 320)
        self.write(f"Score = {self.score}", False, "center", ("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", False, "center", ("Arial", 18, "normal"))
