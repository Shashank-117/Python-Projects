from turtle import Turtle, Screen
t = Turtle()
screen = Screen()
screen.colormode(255)
import random
#import colorgram
#colors = colorgram.extract('hirst painting.jpg', 20)
#final_colors = []
#for color in colors:
    #r = color.rgb.r
    #g = color.rgb.g
    #b = color.rgb.b
    #new_color = (r, g, b)
    #final_colors.append(new_color)

#print(final_colors)
color_list = [(236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]
t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)
for p in range(0, 10):

    for i in range(0, 10):
        c = random.choice(color_list)
        t.color(c[0], c[1], c[2])
        t.dot(20)
        t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(500)
    t.left(180)



screen.exitonclick()