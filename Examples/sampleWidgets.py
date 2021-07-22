# This is a full example containing almost every widget available in tkinter

import tkinter as tk
from tkstylesheet import TkssTheme


def changeTheme():
    global darkTheme
    darkTheme = not darkTheme
    print("Dark theme: ", darkTheme)
    if not darkTheme:
        theme.loadStyleSheet("Themes/lighttheme.tkss")

    else:
        theme.loadStyleSheet("Themes/darktheme.tkss")


def top_level():
    top = tk.Toplevel(root)
    top_lbl = tk.Label(top, text="Top level")
    top_lbl.pack()

    tk.Button(top, text="changeTheme", command=changeTheme).pack()

    theme.reloadStyleSheet()


def initLeftFrame():
    leftlbl = tk.Label(left_frame, text="Left Frame")
    leftlbl.object_id = "leftlabel"
    leftlbl.pack()

    left_lblFrame = tk.LabelFrame(left_frame, text="This is a label frame")
    left_lblFrame.pack(fill="both", expand=True)

    ent_lbl_frame = tk.Frame(left_lblFrame)
    ent_lbl_frame.pack()

    tk.Label(ent_lbl_frame, text="Entry: ").pack(side='left')
    tk.Entry(ent_lbl_frame).pack(side='left', fill='x', expand=True)

    var = tk.StringVar()
    var.set("option1")
    options = ["option1", "option2", "option3"]
    tk.OptionMenu(left_lblFrame, var, *options).pack()

    tk.Spinbox(left_lblFrame, from_=0, to=25).pack()
    tk.Scale(left_lblFrame, variable=tk.IntVar(), from_=1, to=50, orient='horizontal', tickinterval=20, resolution=2)\
        .pack(fill='x', expand=True)

    tk.Message(left_lblFrame, text="This is a message label").pack()

    tk.Button(left_lblFrame, text="Top-level Button", command=top_level).pack()
    tk.Checkbutton(left_lblFrame, text="Check Button").pack()
    tk.Radiobutton(left_lblFrame, text="Radio Button").pack()


def initRightFrame():
    right_lbl = tk.Label(right_frame, text="Right Frame")
    right_lbl.object_id = "rightlabel"
    right_lbl.pack()
    canvas = tk.Canvas(right_frame, height=50)
    canvas.create_text(80, 20, text="This is a canvas", fill='red', font=("Ariel", 15))
    canvas.pack()
    tk.Text(right_frame, height=10).pack()

    scrollbar = tk.Scrollbar(right_frame)
    scrollbar.pack(side='right', fill='y')

    mylist = tk.Listbox(right_frame, yscrollcommand=scrollbar.set)
    for line in range(100):
        mylist.insert('end', "This is line number " + str(line))

    mylist.pack(side='left', fill='both', expand=True)
    scrollbar.config(command=mylist.yview)


root = tk.Tk()

darkTheme = True

menubar = tk.Menu(root)
root.config(menu=menubar)
file = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label="File", menu=file)

file.add_command(label="New", command=None)
file.add_command(label="Open", command=None)

paned_window = tk.PanedWindow(root, handlesize=4, orient=tk.HORIZONTAL)
paned_window.pack(expand=True, fill="both")

left_frame = tk.Frame(paned_window)
right_frame = tk.Frame(paned_window)

paned_window.add(left_frame, width=200)
paned_window.add(right_frame)

initLeftFrame()
initRightFrame()

theme = TkssTheme(root)
theme.loadStyleSheet("Themes/darktheme.tkss")

root.mainloop()
