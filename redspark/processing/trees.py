class Element:
    def __init__(self, label, color=None):
        self.label = label
        self.color = color

    def __str__(self):
        return self.ansi_colored(self.label, self.color)

    @staticmethod
    def ansi_colored(text, argb):
        if argb is None:
            return text
        r = (argb >> 16) & 0xFF
        g = (argb >> 8) & 0xFF
        b = argb & 0xFF
        return f"\x1b[38;2;{r};{g};{b}m{text}\x1b[0m"


class Tree:
    def __init__(self, *children, label, color=None):
        self.label = label
        self.children = list(children)
        self.color = color

    def __str__(self):
        return Element.ansi_colored(self.label, self.color)

    def render(self, prefix=""):
        lines = [str(self)]
        last_index = len(self.children) - 1
        for i, child in enumerate(self.children):
            is_last = (i == last_index)
            connector = " └── " if is_last else " ├── "
            extension = "     " if is_last else " │   "

            if isinstance(child, Tree):
                lines.append(prefix + connector + str(child))
                subtree = child.render(prefix + extension).splitlines()[1:]
                lines.extend(subtree)
            else:
                lines.append(prefix + connector + str(child))
        return "\n".join(lines)
