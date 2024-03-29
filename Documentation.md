### Quickstart

Here is a quick example to get you started.

```py
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
read more examples [here](https://github.com/PaulleDemon/tkStyleSheet/tree/master/Examples)

### TkThemeLoader class


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

### Stylesheet syntax

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

**Using Id's:**
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

**wildcard:**
    using `*` is considered wild card which will apply stylesheet to all the widgets.

```
*{
    background: "red";
}
```
The above stylesheet will ensure that all the widgets will have `red` background.

**Debugging stylesheet:**

For easier debugging of stylesheet `TkStyleSheetError` will be raised if there is a problem in the stylesheet. 
It will also mention were the problem could be.

#### Important note on how stylesheets are applied
 * The style sheet is applied sequentially. So you override a selector it will inherit the property
    the previous selector requiring you to override the selector properties.
   
Example:
```
Label{
    foreground: "red";
    background: "white";
}
        
Label{
    background: "blue";
}    
```    
On applying this stylesheet you will notice that the label has `red` foreground and `blue` background and not `white`

* Also, make sure you create the `TkThemeLoader(widget)` after you create all the child widgets. Else stylesheet might not be applied as expected. 
  You can also reload the stylesheets if they are created dynamically or if you created the theme instances at the beginning by using `theme.reloadStyleSheet()` method, this 
  will reload your stylesheet and apply the style to the new widgets that are created later on or during runtime.

To get the available options for each widget's read [themeOptions](theme_options.tkss). (note: some options are undocumented)
