import re
import ast

style = """
        Label{
        activebackground: "#ffffff";
        activeforeground: "#000000";
        anchor: "center"; /*available anchors: nw, ne, n, w, e, sw, s, se*/
        foreground: "#ffffff";
        }
        
        Button{
        activebackground: "#ffffff";
        activeforeground: "#000000";
        anchor: "center"; /*available anchors: nw, ne, n, w, e, sw, s, se*/
        foreground: "#ffffff";
        }
        
        """


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
                raise SyntaxError(f"Syntax in {key} near '{key_}: {value}'")

            new_dict[key_] = value

        # print(new_dict)

        key_words[key] = new_dict

    # print(key_words)

    return key_words


parse()
