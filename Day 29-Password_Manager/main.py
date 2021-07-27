from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def Password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters= int(random.randint(8, 10))
    nr_symbols = int(random.randint(2, 4))
    nr_numbers = int(random.randint(2, 4))

    password_list = []

    password_list += [random.choice(letters) for q in range (1,nr_letters+1)]

    password_list +=[random.choice(symbols) for q in range (1,nr_symbols+1)]

    password_list +=[random.choice(numbers) for q in range (1,nr_numbers+1)]


    random.shuffle(password_list)

    password = ''.join(password_list)
    print(password)
    #saves password on clipboard
    pyperclip.copy(password)
    entry_password.insert(0, f'{password}')



# ---------------------------- SAVE PASSWORD ------------------------------- #

def Add():
    password = entry_password.get()
    username = entry_username.get()
    website = entry_website.get()
    if len(password) == 0 or len(username) == 0 or len(website) == 0:
        messagebox.showinfo(message='You left a field blank, Please fill to continue', title="Can't Continue !!!")
    else:
        is_ok = messagebox.askokcancel(message=f'Website : {website}\nUsername : {username}\nPassword : {password}\nAre you sure?', title='Are you sure?')

        if is_ok == True:
            with open(file='database.txt', mode='a') as data:
                data.write(f'{website} | {username} | {password}\n')

            entry_website.delete(0, END)
            entry_username.delete(0, END)
            entry_password.delete(0, END)
            entry_website.focus()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=40, pady=40)
window.title('Password Generator')

image = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

label_1 = Label(text='Website:')
label_1.grid(row=1, column=0)

label_2 = Label(text='Email/Username:')
label_2.grid(row=2, column=0)

label_3 = Label(text='Password:')
label_3.grid(row=3, column=0)

entry_website = Entry(width=45)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_username = Entry(width=45)
entry_username.grid(row=2, column=1, columnspan=2)

entry_password = Entry(width=25)
entry_password.grid(row=3, column=1)

button_generate = Button(text='Generate Password', width=15, command=Password)
button_generate.grid(row=3, column=2)

button_add = Button(width=45, text='Add', command=Add)
button_add.grid(row=4, column=1, columnspan=2)

window.mainloop()

