"""Create a Label Widget"""
"""Set Label Font Size"""
from tkinter import *

window = Tk()
window.geometry("1000x700")
window.title("Welcome to LikeGeeks app")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
window.mainloop()
