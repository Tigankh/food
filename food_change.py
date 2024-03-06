import json
import tkinter
from tkmacosx import Button
from data import lst
import os

window = tkinter.Tk()
window.title("food_change_next")
window.geometry("700x700")

if os.path.isfile('save.json'):
    with open('save.json', 'r') as file:
        count = json.load(file)
else:
    count = 0
label = tkinter.Label(window, text=lst[count])
label.place(x=100, y=100, width=200)

btn = tkinter.Button(window, text="next", background='green', command=lambda: change_label(label))
btn.place(x=350, y=100, width=200)


def change_label(label: tkinter.Label):
    global count
    count += 1
    label.config(text=str(lst[count % len(lst)]))
    with open('save.json', 'w') as file:
        json.dump(count, file)


window.mainloop()
