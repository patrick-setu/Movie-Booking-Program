import tkinter as tk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

# Importing image
img = tk.PhotoImage(file="img.png")

class create_button:

    def __init__(self, location, fg, x, y, state = "normal"):
        self.location = location
        self.fg = fg
        self.x = x
        self.y = y
        self.state = state
        self.but = tk.Button(self.location, fg = self.fg,
                             state=self.state, height = 1, command=None,
                             borderwidth=0)
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

window = None

# Creating and configuring root window settings

seats_screen = tk.Frame(window, bg=bg_col)
seats_screen.pack(expand=True, fill="both")

# Creating overall frames widgets
image = tk.Label(window, text = 'Ajahy', bg=bg_col)
image.place(relx=0.5, rely=0.5, anchor="center")