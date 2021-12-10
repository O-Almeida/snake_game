from turtle import Turtle
import random

MAX_VALUE = 340
possible_xy = [x for x in range(-MAX_VALUE, MAX_VALUE, 20)]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.generate()

    def generate(self):
        self.goto(possible_xy[random.randint(0, len(possible_xy) - 1)],
                  possible_xy[random.randint(0, len(possible_xy) - 1)])
        print(self.pos())
