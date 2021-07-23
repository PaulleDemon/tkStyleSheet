import re
import ast
import tkinter as tk


class TkStyleSheetError(Exception):
    pass


class TkssTheme:
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
        "SpinBox": set(),
        "OptionMenu": set(),
        "Canvas": set(),
        "TopLevel": set(),
        "Message": set(),
        "Menu": set(),
        "MenuButton": set(),
        "ScrollBar": set(),
        "Text": set()
    }

    def __init__(self, parent):
        self.parent = parent
        self._style_sheet = ""
        self.append(parent)
        self._findChildren(parent)

    def _findChildren(self, parent):

        for child in parent.winfo_children():
            self.append(child)
            self._findChildren(child)

    def append(self, widget):

        """ Appends widget to correct key"""

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
            self.widgets["SpinBox"].add(widget)

        elif isinstance(widget, tk.OptionMenu):
            self.widgets["OptionMenu"].add(widget)

        elif isinstance(widget, tk.Canvas):
            self.widgets["Canvas"].add(widget)

        elif isinstance(widget, tk.Toplevel):
            self.widgets["TopLevel"].add(widget)

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
        # print(file_path)
        with open(file_path, 'r') as fobj:
            style_sheet = fobj.read()

        self.setStylesheet(style_sheet)

    def styleSheet(self) -> str:
        """ returns the current stylesheet"""
        return self._style_sheet

    def reloadStyleSheet(self):
        """ reloads the widgets and the styles sheets. Call this if you are dynamically creating widgets"""
        # for x in self.widgets:  # not necessary as set removes duplicates
        #     self.widgets[x] = set()

        self._findChildren(self.parent)
        self.setStylesheet(self._style_sheet)

    def setStylesheet(self, stylesheet: str):
        """ sets the style sheet """
        keywords = parsetkss(stylesheet)
        # print(keywords)
        self._style_sheet = stylesheet
        # print(self.widgets)
        for key, values in keywords.items():
            print(key)
            selector = key.split("#")
            # print(selector)
            try:

                for x in self.widgets[selector[0]].copy():
                    # print("selector: ", selector, x, values)
                    try:
                        if len(selector) == 2:
                            try:
                                if x.object_id == selector[1]:
                                    x.config(values)

                            except AttributeError:
                                continue

                        else:
                            x.config(values)

                    except tk.TclError as e:
                        print("ERROR: ", e)
                        if "unknown option" in f"{e}":
                            raise TkStyleSheetError(f"{e} in '{key}'")

                        elif "invalid command name" in f"{e}":
                            self.widgets[selector[0]].remove(x)

                        else:
                            raise tk.TclError(e)

            except KeyError:
                raise TkStyleSheetError(f"Unknown widget '{key}'")


def parsetkss(stylesheet: str = "") -> dict:
    """ parses the tkss to dictionary"""

    new_line_replace = stylesheet.replace("\n", "")
    space_replace = re.sub(r"\s+", "", new_line_replace, flags=re.UNICODE)
    comments_removed = re.sub(r"/\*(.|\n)*?\*/", '', space_replace)

    split_brackets = re.split(r"[{}]", comments_removed)
    option_values = [(split_brackets[x], split_brackets[x + 1]) for x in range(0, len(split_brackets) - 1, 2)]

    for index, (key, values) in enumerate(option_values.copy()):  # evaluates expressions like Label, Button{}

        _key = key.split(',')
        if len(_key) > 1:
            option_values.remove((key, values))

            for x in _key:
                option_values.insert(index+1, (x, values))

    # print("Option values: ", option_values)
    new_options_values = {x: {} for (x, y) in option_values}

    for key, property in option_values.copy():
        # print("KEY: ", key)
        new_dict = {}
        word = property.split(';')

        try:
            word.remove('')

        except ValueError:
            raise TkStyleSheetError(f"Error in or near '{key}'")

        for x in word:
            word_split = x.split(':')
            key_ = word_split[0].replace("cursorbackground", "insertbackground") \
                .replace("cursorborderwidth", "insertborderwidth").replace("cursorwidth", "insertwidth")

            value = word_split[1].replace("\"", "\'")

            try:
                value = ast.literal_eval(value)

            except SyntaxError:
                raise TkStyleSheetError(f"Syntax error near '{key}{{...{key_}: {value}...}}'")

            new_dict[key_] = value

        # print(new_dict.items())

        new_options_values[key].update(new_dict)
        # new_options_values.update({key: new_dict})

    import pprint
    pprint.pprint(new_options_values)

    return new_options_values
