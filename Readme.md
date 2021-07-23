# Tkinter stylesheet - Tkss

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

This library helps you to set style to tkinter default widget using stylesheet without
much work.

**Quick Example:**

```python
from tkinter import *
from tkstylesheet import TkThemeLoader

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

theme = TkThemeLoader(root)
theme.setStylesheet(_style)  # pass as string

root.mainloop()
```

If you want to load tkss from a file:

1. save you theme in a file
2. load it using TkThemeLoader().loadStyleSheet(file_path)

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
from tkstylesheet import TkThemeLoader

root = Tk()

Label(root, text="label").pack()
Button(root, text="Button").pack()

theme = TkThemeLoader(root)
theme.loadStyleSheet("theme.tkss")  # pass file path

root.mainloop()
```

Please read further examples on how to switch theme etc, [here](https://github.com/PaulleDemon/tkStyleSheet/tree/master/Examples).
Refer stylesheets examples [here](https://github.com/PaulleDemon/tkStyleSheet/tree/master/Examples/Themes)

Documentation [here](https://github.com/PaulleDemon/tkStyleSheet/blob/master/Documentation.md)