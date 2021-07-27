from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.s = 0
        self.speed('fastest')
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        with open('high_score.txt', mode='r') as file:
            self.high = int(file.read())
        self.update()



    def update(self):
        self.clear()
        self.write(f'Score : {self.s}  High Score : {self.high}', False, 'center', 'Arial')

    def score(self):
        self.s += 1
        self.update()
        self.HighScore()

    def over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center', 'Arial')

    def HighScore(self):
        if self.s > self.high:
            with open('high_score.txt', mode='w') as file:
                file.write(str(self.s))

