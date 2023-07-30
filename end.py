"""Import tkinter for GUI."""
import tkinter as tk
import sys

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

# Creating and configuring root window settings
window = None
end = tk.Frame(window, bg=bg_col)


class Place:
    """Widget placing class shorthand."""

    def __init__(self, widget, x, y, anchor="center"):
        """Place widget based on x, y."""
        self.widget = widget
        self.x = x
        self.y = y
        self.anchor = anchor
        self.widget.place(relx=self.x, rely=self.y, anchor=self.anchor)


class CreateButton:
    """Create instance of a button."""

    def __init__(self, location, text, fg, bg, x, y, comm=None):
        """Stylise the button."""
        self.location = location
        self.text = text
        self.fg = fg
        self.bg = bg
        self.x = x
        self.y = y
        self.comm = comm
        self.but = tk.Button(
            self.location,
            bg=self.bg,
            text=self.text,
            fg=self.fg,
            command=self.comm,
            height=1,
            width=15,
            borderwidth=0,
            highlightbackground=bg_col,
            font=(font_name, 16),
        )
        self.but.place(relx=self.x, rely=self.y, anchor="center")


# Page widgets

text = tk.Label(
    end,
    fg=fg_col,
    bg=btn_col,
    font=(font_name, 25),
    wraplength=400,
    width=30,
    height=12,
)
Place(text, 0.5, 0.45)

CreateButton(end, "Close page", fg_col, btn_col, 0.5, 0.9, lambda: sys.exit())
