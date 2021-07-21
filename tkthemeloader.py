import tkinter as tk
import tssparser

class Theme:

    widgets = {"Label": set(),
               "Button": set(),
               "Entry": set(),
               "CheckButton": set(),
               "RadioButton": set(),
               "Scale": set(),
               "ListBox": set(),
               "Frame": set(),
               "LabelFrame": set(),
               "PanedWindow": set(),
               "Spinbox": set(),
               "OptionMenu": set(),
               "Canvas": set(),
               "Toplevel": set(),
               "Message": set(),
               "Menu": set(),
               "MenuButton": set(),
               "ScrollBar": set(),
               "Text": set()
               }

    def __init__(self, parent):
        self.parent = parent
        self.style_sheet = ""
        self.findChildren(parent)

    def findChildren(self, parent):

        for child in parent.winfo_children():
            self.append(child)
            grand_child = child.winfo_children()
            while grand_child:
                for x in grand_child:
                    grand_child = x.winfo_children()
                    self.append(x)

        # print(self.widgets)

    def append(self, widget):

        if isinstance(widget, tk.Label):
            self.widgets["Label"].add(widget)

        elif isinstance(widget, tk.Button):
            self.widgets["Button"].add(widget)

        elif isinstance(widget, tk.Entry):
            self.widgets["Entry"].add(widget)

        elif isinstance(widget, tk.Checkbutton):
            self.widgets["CheckButton"].add(widget)

        elif isinstance(widget, tk.Radiobutton):
            self.widgets["RadioButton"].add(widget)

        elif isinstance(widget, tk.Scale):
            self.widgets["Scale"].add(widget)

        elif isinstance(widget, tk.Listbox):
            self.widgets["ListBox"].add(widget)

        elif isinstance(widget, tk.Frame):
            self.widgets["Frame"].add(widget)

        elif isinstance(widget, tk.LabelFrame):
            self.widgets["LabelFrame"].add(widget)

        elif isinstance(widget, tk.PanedWindow):
            self.widgets["PanedWindow"].add(widget)

        elif isinstance(widget, tk.Spinbox):
            self.widgets["Spinbox"].add(widget)

        elif isinstance(widget, tk.OptionMenu):
            self.widgets["OptionMenu"].add(widget)

        elif isinstance(widget, tk.Canvas):
            self.widgets["Canvas"].add(widget)

        elif isinstance(widget, tk.Toplevel):
            self.widgets["Toplevel"].add(widget)

        elif isinstance(widget, tk.Message):
            self.widgets["Message"].add(widget)

        elif isinstance(widget, tk.Menu):
            self.widgets["Menu"].add(widget)

        elif isinstance(widget, tk.Menubutton):
            self.widgets["MenuButton"].add(widget)

        elif isinstance(widget, tk.Scrollbar):
            self.widgets["ScrollBar"].add(widget)

        elif isinstance(widget, tk.Text):
            self.widgets["Text"].add(widget)

        else:
            print(f"Unknown widget: {widget}")

    def loadStyleSheet(self, file_path):
        """ provide a valid path to style sheet and it will be set"""
        print(file_path)
        with open(file_path, 'r') as fobj:
            style_sheet = fobj.read()

        print("Sheet: ", style_sheet)
        self.setStylesheet(style_sheet)

    def styleSheet(self) -> str:
        """ returns the current stylesheet"""
        return self.style_sheet

    def setStylesheet(self, stylesheet: str):
        keywords = tssparser.parse(stylesheet)
        print(stylesheet)
        self.style_sheet = stylesheet

        for key, values in keywords.items():
            print("KEY: ", key)
            for x in self.widgets[key]:
                x.config(values)