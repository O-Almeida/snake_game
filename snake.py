from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.initialize(MOVE_DISTANCE)

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
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        first_seg = self.segments[0]
        second_seg = self.segments[1]
        if first_seg.ycor() == second_seg.ycor():
            if first_seg.xcor() > second_seg.xcor():
                first_seg.left(90)
            else:
                first_seg.right(90)

    def down(self):
        first_seg = self.segments[0]
        second_seg = self.segments[1]
        if first_seg.ycor() == second_seg.ycor():
            if first_seg.xcor() > second_seg.xcor():
                first_seg.right(90)
            else:
                first_seg.left(90)

    def left(self):
        first_seg = self.segments[0]
        second_seg = self.segments[1]
        if first_seg.ycor() != second_seg.ycor():
            if first_seg.ycor() < second_seg.ycor():
                first_seg.right(90)
            else:
                first_seg.left(90)

    def right(self):
        first_seg = self.segments[0]
        second_seg = self.segments[1]
        if first_seg.ycor() != second_seg.ycor():
            if first_seg.ycor() < second_seg.ycor():
                first_seg.left(90)
            else:
                first_seg.right(90)

