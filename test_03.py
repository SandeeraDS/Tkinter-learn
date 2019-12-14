"""Adding a Button Widget"""
"""Change Button Foreground and Background Colors"""
from tkinter import *

window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('1000x700')
lbl = Label(window, text="Hello")
lbl.grid(column=10, row=0)
btn = Button(window, text="Click Me", bg="orange", fg="red")
btn.grid(column=1, row=1)
window.mainloop()
