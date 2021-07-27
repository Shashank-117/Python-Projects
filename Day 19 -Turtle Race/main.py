from turtle import Turtle, Screen
import random
screen = Screen()
bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? pick a color.')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_pos = [-70, -40, -10, 20, 50, 80]
screen.setup(500, 400)
all_turtles = []
for index in range (0, 6):
    t =Turtle(shape='turtle')
    t.penup()
    t.color(colors[index])
    t.goto(-230, y_pos[index])
    all_turtles.append(t)

if bet:
    race = True
else:
    race = False
    print("Invalid Entry")

while race == True:
    for turtle in all_turtles:
        distance = random.randint(0, 10)
        turtle.forward(distance)
        if turtle.xcor() >= 230:
            race = False
            winner = turtle.pencolor()

if bet == winner:
    print(f"You've won !!! {winner} color turtle won")
else:
    print(f"You've lost !!! {winner} color turtle won")



screen.exitonclick()