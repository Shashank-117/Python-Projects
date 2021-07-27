import turtle
import pandas
screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
missed = []
i = 0
already_guessed = []
data = pandas.read_csv('50_states.csv')
while i < 50:
    answer = screen.textinput(title=f'{i}/50 States Guessed', prompt="Enter a state's name")
    answer = answer.title()
    if answer == 'Exit':
        break
    all_states = data.state.to_list()
    if answer in all_states and answer not in already_guessed:

        i += 1
        a = data[data.state == answer]
        t = turtle.Turtle()
        already_guessed.append(a.state.item())
        print(already_guessed)
        t.penup()
        t.hideturtle()
        t.speed('fastest')
        t.goto(int(a.x), int(a.y))
        t.write(answer)

for state in all_states:
    if state not in already_guessed:
        missed.append(state)

missed_dict = {
    'states missed' : missed
}

m = pandas.DataFrame(missed_dict)

m.to_csv('missed_states')