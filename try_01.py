import time
import tkinter
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk

# get window object
window = tkinter.Tk()
# set window size
window.geometry('1040x550')
# add background image
background_image = tkinter.PhotoImage(file="3.png")
# set background image
background_label = tkinter.Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
# add title to app
window.title("Note Generator for Lecture Video")


def add_text(text, dir_type):
    if dir_type == 0:
        loc_video.delete(0, tkinter.END)
        loc_video.insert(0, text)
        return
    elif dir_type == 1:
        loc_transcript.delete(0, tkinter.END)
        loc_transcript.insert(0, text)
    else:
        loc_save_to.delete(0, tkinter.END)
        loc_save_to.insert(0, text)


def select_file_type(dir_type=2):
    if dir_type == 0:
        file_path = filedialog.askopenfile(filetypes=(("mp4 files", "*.MP4"), ("all files", "*.*")))
        add_text(file_path.name, dir_type)
    elif dir_type == 1:
        file_path = filedialog.askopenfile(filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        add_text(file_path.name, dir_type)
    else:
        file_path = filedialog.askdirectory()
        add_text(file_path, dir_type)


# label video location
label_video = tkinter.Label(window, text="Video Location", font=("Helvetica", 15, "bold"), bg="silver", fg="black")
label_video.place(x=50, y=100)
# text entry for video location
loc_video = tkinter.Entry(window, width=75)
loc_video.place(x=350, y=105)
# button for open file explore
icon_1 = tkinter.PhotoImage(file="icon1.png")
select_video = tkinter.Button(window, image=icon_1, bg="silver", command=lambda: select_file_type(0))
select_video.place(x=960, y=103)

# label transcript location
label_transcript = tkinter.Label(window, text="Transcript Location", font=("Helvetica", 15, "bold",), bg="silver",
                                 fg="black")
label_transcript.place(x=50, y=180)
# text entry for transcript location
loc_transcript = tkinter.Entry(window, width=75)
loc_transcript.place(x=350, y=185)

select_transcript = tkinter.Button(window, image=icon_1, bg="silver", command=lambda: select_file_type(1))
select_transcript.place(x=960, y=183)

# label save location
label_save_to = tkinter.Label(window, text="Save Note To", font=("Helvetica", 15, "bold",), bg="silver",
                              fg="black")
label_save_to.place(x=50, y=260)

# text entry for save location
loc_save_to = tkinter.Entry(window, width=75)
loc_save_to.place(x=350, y=265)

select_save_directory = tkinter.Button(window, image=icon_1, bg="silver", command=select_file_type)
select_save_directory.place(x=960, y=263)


# method for progress bar
def bar():
    progress['value'] = 20
    window.update_idletasks()
    time.sleep(1)
    progress['value'] = 50
    window.update_idletasks()
    time.sleep(1)
    progress['value'] = 80
    window.update_idletasks()
    time.sleep(1)
    progress['value'] = 100
    time.sleep(1)
    # if progress completed show completed msg
    if progress['value'] == 100:
        messagebox.showinfo("Information", "Lecture Note Created Successfully !")
        progress['value'] = 0


# button for start generation of note
btn_generate = tkinter.Button(window, text="Generate Note", font=("Helvetica", 15, "bold"), bg="silver", fg="black",
                              command=bar)
btn_generate.place(x=450, y=350)
btn_generate['state'] = "disabled"

# location of the progress bar
progress = ttk.Progressbar(window, orient=tkinter.HORIZONTAL, length=500, mode='determinate')
progress.place(x=270, y=420)

window.mainloop()
