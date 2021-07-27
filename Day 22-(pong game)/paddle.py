from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.segments = []
        self.penup()
        self.speed('fastest')
        self.shape('square')
        self.shapesize(1, 5)
        self.goto(x, y)
        self.color('white')
        self.setheading(90)


    def go_up(self):
        self.forward(40)

    def go_down(self):
        self.backward(40)