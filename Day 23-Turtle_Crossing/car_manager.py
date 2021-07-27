COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
from turtle import Turtle


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.m = STARTING_MOVE_DISTANCE

    def create(self):
        chance = random.randint(1, 6)
        if chance == 1:
            car = Turtle()
            car.shape('square')
            car.color(random.choice(COLORS))
            car.penup()
            car.shapesize(1, 2)
            y = random.randint(-250, 250)
            x = 310
            car.setheading(180)
            car.goto(x, y)
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.m)

    def new_lvl(self):
        self.m += MOVE_INCREMENT
