# Tkinter stylesheet - Tkss

[![License](https://img.shields.io/badge/License%20-MIT-green.svg?style=flat&colorA=#1af041&colorB=007D8A)](https://opensource.org/licenses/MIT)


This library helps you to write set style to tkinter default widget using stylesheet without
much work.

**Quick Example:**

```python
from tkinter import *
from tkstylesheet import Theme

_style = """
        Tk{
            background: "#565657"; /*background color of the root widget*/
        }
        
        Label{
            foreground: "#ebebeb";
            background: "#565657";
        }
        
        Button{
            foreground: "#ebebeb";
            background: "#565657";
        }
        
        """

root = Tk()

Label(root, text="label").pack()
Button(root, text="Button").pack()

theme = Theme(root)
theme.setStylesheet(_style)  # pass as string

root.mainloop()
```

If you want to load tkss from a file:

1. save you theme in a file
2. load it using Theme().loadStyleSheet(file_path)

example:

theme.tkss
```
Tk{
    background: "#565657";
}

Label{
    foreground: "#ebebeb";
    background: "#565657";
}

Button{
    foreground: "#ebebeb";
    background: "#565657";
}
```
project.py

```python
from tkinter import *
from tkstylesheet import Theme

root = Tk()

Label(root, text="label").pack()
Button(root, text="Button").pack()

theme = Theme(root)
theme.loadStyleSheet("theme.tkss")  # pass file path

root.mainloop()
```

Please read further examples on how to switch theme etc. [here](Examples)

