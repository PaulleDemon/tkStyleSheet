# Tkss Documentation:

### TkssTheme class:


| Methods             |               Arguments     |   Description                                                                          |
| -----------         | -----------                 |-------                                                                                 |
| append              |   widget (tkinter widget)   | appends the tkinter widgets to correct key                                             | 
| loadStyleSheet      |   file_path                 | reads stylesheet from the file and loads it                                            | 
| styleSheet          |   -                         | returns the current stylesheet                                                         | 
| reloadStyleSheet    |   -                         | reloads the widgets widgets ad stylesheet (useful when you dynamically create widgets) | 
| setStylesheet       |   stylesheet (string)       | sets the stylesheets                                                                   | 

Available widgets and their equivalent stylesheet name:

| tkinter widgets     |      Equivalent             |                                                                
| -----------         | -----------                 |
|      Tk             |        Tk                   |
|      Label          |        Label                |
|      Button         |        Button               |
|      Entry          |        Entry                |
|      Checkbutton    |        CheckButton          |
|      Radiobutton    |        RadioButton          |
|      Scale          |        Scale                |
|      Listbox        |        ListBox              |
|      Frame          |        Frame                |
|      LabelFrame     |        LabelFrame           |
|      PanedWindow    |        PanedWindow          |
|      Spinbox        |        SpinBox              |
|      OptionMenu     |        OptionMenu           |
|      Canvas         |        Canvas               |
|      Toplevel       |        TopLevel             |
|      Message        |        Message              |
|      Menu           |        Menu                 |
|      Menubutton     |        MenuButton           |
|      Scrollbar      |        ScrollBar            |
|      Text           |        Text                 |

> note: Style sheet will be applied to the children of the provided parent (in the init method).

### Stylesheet syntax:

**To style a widget:**
```
Widgetname{
    background: "#ffffff"; /*background color of the widget*/
}
```
**Comments:**
```
/*This is an example of comment which will be ignored*/
```

**Selectors:**
    You can add styles to specific widgets using `widgetname#object_id`

python:
```python
label = tk.Label(parent)
label.object_id = "selectlabel"
```
Stylesheet:
```
Label#selectlabel{
    background: "#000000";
}
```

`[tkinterWidget].object_id = "objectid"` should be used for this to take effect.
No spaces allowed in the "objectid".

>Note: object id doesn't have to be unique. Multiple widgets can have the same id,
> and it will be applied to all the widget that have the same object id.

**Debugging stylesheet:**

For easier debugging of stylesheet `TkStyleSheetError` will be raised if there is a problem in the stylesheet. 
It will also mention were the problem could be.