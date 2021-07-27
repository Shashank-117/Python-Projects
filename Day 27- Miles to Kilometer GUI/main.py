from tkinter import *
window = Tk()
window.title('MILES to KM convertor')
window.config(padx=20, pady=20)

label = Label(text='is equal to')
label.grid(row=2, column=1)

label1 = Label(text='Miles')
label1.grid(row=1, column=3)

label2 = Label(text='Kilometers')
label2.grid(row=2, column=3)

label_answer = Label(text='0')
label_answer.grid(row=2, column=2)

entry = Entry(width=7)
entry.insert(END, string='0')
entry.grid(row=1, column=2)

def calculate():
    x = float(entry.get())
    x *= 1.609
    x = round(x, 2)
    label_answer.config(text=x)


button = Button(text='Calculate', command=calculate)
button.grid(row=3, column=2)

window.mainloop()