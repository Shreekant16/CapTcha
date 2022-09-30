from tkinter import *
import random

window = Tk()
window.geometry('200x100')

def cap():
    alphabets = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    c = []
    for i in range(4):
        c.append(random.choice(alphabets))
    for i in range(2):
        c.append(random.choice(numbers))

    random.shuffle(c)
    label.config(text=f'{"".join(c)}')



button = Button(text="Cpatcha", command=cap)
button.grid(column=1, row=0)

label = Label(text="XXX")
label.grid(column=1, row=2)

window.mainloop()
