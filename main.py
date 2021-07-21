import tkinter as tk
from tkthemeloader import Theme

style = """
        Label{
        activebackground: "#ffffff";
        activeforeground: "#000000";
        anchor: "center"; /*available anchors: nw, ne, n, w, e, sw, s, se*/
        foreground: "#ffffff";
        background: "#000000";
        }

        Button{
        activebackground: "#ffffff";
        activeforeground: "#000000";
        anchor: "center"; /*available anchors: nw, ne, n, w, e, sw, s, se*/
        foreground: "#ffffff";
        }

        """

root = tk.Tk()

tk.Label(root, text="label").pack(expand=1, fill='both')
tk.Button(root, text="Button").pack(expand=1, fill='both')
tk.Checkbutton(root, text="Check Button").pack(expand=1, fill='both')
tk.Radiobutton(root, text="Radio Button", value=1).pack(expand=1, fill='both')
tk.Entry(root).pack(expand=1, fill='both')
tk.Scale(root, orient=tk.HORIZONTAL).pack(expand=1, fill='both')

listbox = tk.Listbox(root)
listbox.pack(expand=1, fill='both')

for item in ["ListBox","three","four","five"]:
    listbox.insert(tk.END, item)

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")
tk.Label(frame, text="Frame Label").pack(expand=True, fill="both")

frame_lbl = tk.LabelFrame(root, text="Label rame")
frame_lbl.pack(expand=True, fill="both")
lbl = tk.Label(frame_lbl, text="Label Frame")
lbl.pack(expand=True, fill="both")
tk.Label(lbl, text="Label Frame2").pack(expand=True, fill="both")

tk.PanedWindow(root)
# tk.Toplevel(root)

tk.Canvas(root)
tk.Spinbox(root)
tk.OptionMenu(root, value=("1", "2", "3"), variable=tk.StringVar()).pack(expand=True, fill="both")

tk.Menu()
tk.Message()
tk.Menubutton()
tk.Scrollbar()
tk.Text()

theme = Theme(root)
theme.loadStyleSheet(r"theme.txt")

root.mainloop()