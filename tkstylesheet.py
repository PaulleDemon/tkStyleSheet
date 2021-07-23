import re
import ast
import tkinter as tk
import warnings


class TkStyleSheetError(Exception):
    pass


class TkThemeLoader:

    """ reads tk stylesheet and sets it to the widgets"""

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
            warnings.warn(f"Unknown widget: {widget}")

    def loadStyleSheet(self, file_path):
        """ provide a valid path to style sheet and it will be set"""

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
        keywords = _parsetkss(stylesheet)
        self._style_sheet = stylesheet

        for key, values in keywords.items():

            selector = key.split("#")

            try:

                for x in self.widgets[selector[0]].copy():

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

                        if "unknown option" in f"{e}":
                            raise TkStyleSheetError(f"{e} in '{key}'")

                        elif "unknown color name" in f"{e}":
                            raise TkStyleSheetError(f"{e} in '{key}'")

                        elif "invalid command name" in f"{e}":
                            self.widgets[selector[0]].remove(x)  # removes the item it the item has been destroyed

                        else:
                            raise tk.TclError(e)

            except KeyError:
                raise TkStyleSheetError(f"Unknown widget '{key}'")


def _parsetkss(stylesheet: str = "") -> dict:
    """ parses the tkss and returns dictionary"""

    cleanup = re.sub(r"[\n\r\s]+|/\*(.|\n)*?\*/", "", stylesheet)  # removes comments, newlines and white spaces

    sel_dec = re.split(r"[{}]", cleanup)  # separates selector and declaration
    rule_set = [(sel_dec[x], sel_dec[x + 1]) for x in range(0, len(sel_dec) - 1, 2)]

    rule_set = [(','.join(TkThemeLoader.widgets.keys()), y) if x == '*' else (x, y) for (x, y) in rule_set] # replaces wildcard

    for index, (sels, dec) in enumerate(rule_set.copy()):
        # Evaluates expressions like Label, Button{...} and separates them and inserts them as new sel, declaration

        if dec == "":  # removes the element if there is nothing in the declaration block
            rule_set.remove((sels, dec))
            continue

        sel = sels.split(',')  # separating selectors

        if len(sel) > 1:
            for s in sel:
                rule_set.insert(index + 1, (s, dec))

            rule_set.remove((sels, dec))

    new_sel_dec = {x: {} for (x, y) in rule_set}  # creates a dictionary with sel as keys

    for sel, declaration in rule_set.copy():
        temp_dict = {}
        word = declaration.split(';')

        try:
            word.remove('')

        except ValueError:
            raise TkStyleSheetError(f"Error in or near '{sel}'")

        for x in word:

            try:
                word_split = x.split(':')
                tkssproperty = word_split[0].replace("cursorbackground", "insertbackground") \
                    .replace("cursorborderwidth", "insertborderwidth").replace("cursorwidth", "insertwidth")

                value = word_split[1].replace("\"", "\'")

            except IndexError:
                raise TkStyleSheetError(f"Error near '{sel}'")

            try:
                value = ast.literal_eval(value)

            except (SyntaxError, ValueError, IndexError):
                raise TkStyleSheetError(f"Syntax error near '{sel}{{...{tkssproperty}: {word_split[1]}...}}'")

            temp_dict[tkssproperty] = value

        new_sel_dec[sel].update(temp_dict)

    return new_sel_dec
