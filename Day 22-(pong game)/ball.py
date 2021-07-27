from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_move = 10
        self.y_move = 10
        self.color('white')
        self.shape('circle')
        self.penup()
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        if self.ycor() > 280:
            self.y_move = -10
        elif self.ycor() < -280:
            self.y_move = 10

    def paddle_bounce(self):
        if self.xcor() > 0:
            self.x_move = -10
        elif self.xcor() < 0:
            self.x_move = 10
        self.move_speed *= 0.9

    def score(self):
        if self.xcor() > 400 or self.xcor() < -400:
            self.home()
            self.x_move = self.x_move * -1

