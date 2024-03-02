import tkinter
from tkmacosx import Button
from data import lst

window = tkinter.Tk()
window.title("food_change_next")
window.geometry("700x700")

label = tkinter.Label(window, text=lst[0])
label.place(x=100, y=100, width=200)

btn = tkinter.Button(window, text="next")
btn.place(x=350, y=100, width=200)

window.mainloop()