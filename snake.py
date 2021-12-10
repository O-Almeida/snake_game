from turtle import Turtle

MOVE_DISTANCE = 20
DOWN = 270
UP = 90
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.initialize(MOVE_DISTANCE)
        self.head = self.segments[0]

    def initialize(self, x):
        for i in range(3):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.goto(-x * i, 0)
            segment.color("white")
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].pos())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

