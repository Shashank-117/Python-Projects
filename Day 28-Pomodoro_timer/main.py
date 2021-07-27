from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
mrk =''
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps, mrk
    window.after_cancel(timer)
    reps = 0
    mrk = ''
    label_2.config(text=mrk)
    label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(clock, text='00:00')


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        countdown(work_secs)
        label.config(text='Work', fg=RED)
    elif reps % 8 == 0:
        countdown(long_break_secs)
        label.config(text='Break', fg=PINK)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        label.config(text='Break', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global mrk
    global timer
    count_min = int(count/60)
    count_sec = int(count % 60)

    if count_sec < 10:
        count_sec = f'0{count_sec}'

    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(clock, text=f'{count_min}:{count_sec}')

    if count >= 0:
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            mrk += '✔'
            label_2.config(text=mrk)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=image)
clock = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 36, 'bold'), fill='white')
canvas.grid(row=2, column=2)



label = Label(text='Timer', font=(FONT_NAME, 36, 'bold'), fg=GREEN, bg=YELLOW)
label.grid(row=1, column=2)


button_1 = Button(text='Start', command=start_timer)
button_1.grid(row=3, column=1)

button_2 = Button(text='Reset', command=reset_timer)
button_2.grid(row=3, column=3)

label_2 = Label(fg=GREEN, bg=YELLOW)
label_2.grid(row=4, column=2)

window.mainloop()

