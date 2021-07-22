import re
import ast
import tkinter as tk


class TkssError(Exception):
    pass


class Theme:

    widgets = {
               "Tk": set(),
               "Label": set(),
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
        self.append(parent)
        self.findChildren(parent)

    # def findChildren(self, parent):
    #
    #     for child in parent.winfo_children():
    #         self.append(child)
    #         grand_child = child.winfo_children()
    #         print("first: ", grand_child)
    #         while grand_child:
    #             for x in grand_child:
    #                 grand_child = x.winfo_children()
    #                 self.append(x)
    #                 print(x)
    #
    #     print(self.widgets)

    def findChildren(self, parent):

        for x in parent.winfo_children():
            self.append(x)
            self.findChildren(x)

    def append(self, widget):

        if isinstance(widget, tk.Tk):
            self.widgets["Tk"].add(widget)

        elif isinstance(widget, tk.Label):
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

        self.setStylesheet(style_sheet)

    def styleSheet(self) -> str:
        """ returns the current stylesheet"""
        return self.style_sheet

    def setStylesheet(self, stylesheet: str):
        keywords = parse(stylesheet)
        print(keywords)
        self.style_sheet = stylesheet
        print(self.widgets)
        for key, values in keywords.items():
            # print(key)
            for x in self.widgets[key]:
                x.config(values)


def parse(stylesheet="") -> dict:
    new_line_replace = stylesheet.replace("\n", "")
    space_replace = re.sub(r"\s+", "", new_line_replace, flags=re.UNICODE)
    comments_removed = re.sub(r"/\*(.|\n)*?\*/", '', space_replace)

    words = re.split(r"[{}]", comments_removed)
    key_words = {words[x]: words[x + 1] for x in range(0, len(words) - 1, 2)}

    for key, property in key_words.items():
        new_dict = {}
        word = property.split(';')
        word.remove('')
        for x in word:
            word_split = x.split(':')
            key_ = word_split[0].replace("cursorbackground", "insertbackground") \
                .replace("cursorborderwidth", "insertborderwidth").replace("cursorwidth", "insertwidth")

            value = word_split[1].replace("\"", "\'")

            try:
                value = ast.literal_eval(value)

            except SyntaxError:
                raise TkssError(f"Syntax error near '{key}{{...{key_}: {value}...}}'")

            new_dict[key_] = value

        # print(new_dict)

        key_words[key] = new_dict

    # print(key_words)

    return key_words