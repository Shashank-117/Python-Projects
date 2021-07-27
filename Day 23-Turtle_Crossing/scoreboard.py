FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.s = 1
        self.write(f'Level {self.s}',  align='center', font=FONT)

    def score(self):
        self.goto(-200, 250)
        self.clear()
        self.s += 1
        self.write(f'Level {self.s}', align='center', font=FONT)

    def game_over(self):
        self.home()
        self.write('GAME OVER', align='center', font=FONT)