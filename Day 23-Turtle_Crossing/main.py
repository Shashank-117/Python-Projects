import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, 'Up')
game_is_on = True
scoreboard = Scoreboard()
car_manager = CarManager()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create()
    car_manager.move_car()
    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.lvl_up()
        scoreboard.score()
        car_manager.new_lvl()

screen.exitonclick()
