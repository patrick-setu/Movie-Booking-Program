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
end = tk.Frame(window, bg=bg_col, cursor="heart")

class place:
    # Widget placing class shorthand
    def __init__(self, widget, x, y, anchor = "center"):
        self.widget = widget
        self.x = x
        self.y = y
        self.anchor = anchor
        self.widget.place(relx=self.x, rely=self.y, anchor=self.anchor)

class create_button:
    # Makes buttons
    def __init__(self, location, text, fg, bg, x, y, comm = None):
        self.location = location
        self.text = text
        self.fg = fg
        self.bg = bg
        self.x = x
        self.y = y
        self.comm = comm
        self.but = tk.Button(self.location, bg = self.bg, text = self.text,
                             fg=self.fg, command= self.comm, height = 1,
                             width=15, borderwidth=0,
                             highlightbackground=bg_col,
                             font=(font_name, 16))
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

# Page widgets

text = tk.Label(end, text="Booking has been confirmed!\n\n"
                "Thank you for your purchase.\n\n"
                "Check your email at example@email.com to view your tickets",
                fg=fg_col, bg=btn_col, font=(font_name, 35), wraplength=400,
                width=30, height=13)
place(text, 0.5, 0.45)

close = create_button(end, "Close page", fg_col, btn_col, 0.5, 0.9,
                      lambda: sys.exit())