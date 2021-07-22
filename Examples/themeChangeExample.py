from tkinter import *
from tkstylesheet import TkssTheme

_darkthemestyle = """
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

_lightthemestyle = """
        Tk{
            background: "#d9dade"; /*background color of the root widget*/
        }

        Label{
            foreground: "#000000";
            background: "#d9dade";
        }

        Button{
            foreground: "#000000";
            background: "#d9dade";
        }

        """


def changeTheme():
    global dark_theme

    dark_theme = not dark_theme

    if dark_theme:
        theme.setStylesheet(_darkthemestyle)

    else:
        theme.setStylesheet(_lightthemestyle)


root = Tk()

dark_theme = True

Label(root, text="label").pack()
Button(root, text="Change theme", command=changeTheme).pack()

theme = TkssTheme(root)
theme.setStylesheet(_darkthemestyle)

root.mainloop()