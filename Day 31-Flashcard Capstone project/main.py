BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
x = None
dict = None
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title('Flashcard')

#-----------------------------------------------func------------------------------------------#
def new_word():
    global x
    global dict, timer
    window.after_cancel(timer)
    df = pandas.read_csv('data/french_words.csv')
    dict = df.to_dict()
    x = random.randint(0, 101)
    canvas.itemconfig(title, text='French', fill='black')
    canvas.itemconfig(word, text=dict['French'][x], fill='black')
    canvas.itemconfig(bg, image=image_3)
    timer = window.after(3000, eng_word)

def eng_word():
    global x
    global dict
    canvas.itemconfig(title, text='English', fill='white')
    canvas.itemconfig(word, text=dict['English'][x], fill='white')
    canvas.itemconfig(bg, image=image_4)



timer = window.after(3000, eng_word)
#-------------------------------------UI-----------------------------------------------------#

image_1 = PhotoImage(file='images/wrong.png')
button_wrong = Button(width=100, height=100, image=image_1, highlightthickness=0, command=new_word)
button_wrong.grid(row=2, column=0)

image_2 = PhotoImage(file='images/right.png')
button_right = Button(width=100, height=100, image=image_2, highlightthickness=0, command=new_word)
button_right.grid(row=2, column=1)


image_3 = PhotoImage(file='images/card_front.png')
image_4 = PhotoImage(file='images/card_back.png')
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg = canvas.create_image(400, 263, image=image_3)
title = canvas.create_text(400, 150, font=('Ariel', 40, 'italic'), text='title', fill='black')
word = canvas.create_text(400, 263, font=('Ariel', 60, 'bold'), text='word', fill='black')
canvas.grid(row=0, column=0, rowspan=2, columnspan=2)


new_word()


window.mainloop()