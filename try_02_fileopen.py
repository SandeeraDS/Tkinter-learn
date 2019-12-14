import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
# root.withdraw()
root.geometry('1000x550')


# button for start generation of note
def openFile():
    file_path = filedialog.askopenfile(filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
    print(file_path.name)


photo = tk.PhotoImage(file="icon1.png")
btn_generate = tk.Button(root, image=photo, font=("Helvetica", 15, "bold"), bg="silver", fg="black",
                         command=openFile)
btn_generate.place(x=400, y=350)

root.mainloop()
