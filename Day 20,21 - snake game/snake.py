from turtle import Turtle
coor = [(0,0), (-20,0), (-40,0)]
up = 90
down = 270
left = 180
right = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for c in coor:
            self.add_seg(c)


    def add_seg (self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend (self):
        self.add_seg(self.segments[-1].position())

    def move(self):
        for s in range(len(self.segments) - 1, 0, -1):
            x = self.segments[s - 1].xcor()
            y = self.segments[s - 1].ycor()
            self.segments[s].goto(x, y)

        self.segments[0].forward(20)

    def up(self):
        if self.head.heading() != down:
            self.segments[0].setheading(90)

    def down(self):
        if self.head.heading() != up:
            self.segments[0].setheading(270)

    def left(self):
        if self.head.heading() != right:
            self.segments[0].setheading(180)

    def right(self):
        if self.head.heading() != left:
            self.segments[0].setheading(0)