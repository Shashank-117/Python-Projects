from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)
screen.listen()
paddle_right = Paddle(350, 0)
paddle_left = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.onkey(paddle_right.go_up, 'Up')
screen.onkey(paddle_right.go_down, 'Down')
screen.onkey(paddle_left.go_up, 'w')
screen.onkey(paddle_left.go_down, 's')

game_on = True

while game_on == True:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    ball.bounce()
    if ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()
        print('con')
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320:
        ball.paddle_bounce()
        print('Con')
    ball.score()
    if ball.xcor() >= 400:
        scoreboard.score_l()
    if ball.xcor() <= -400:
        scoreboard.score_r()


screen.exitonclick()

