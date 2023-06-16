import tkinter as tk

# Constant
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
font_name = "Yu Gothic Ui Semilight"

# Class

class session_button:

    def __init__(self, location, words, height, width, bg, fg, x, y):
        self.location = location
        self.words = words
        self.height = height
        self.width = width
        self.bg = bg
        self.fg = fg
        self.x = x
        self.y = y
        self.but = tk.Button(self.location, text=self.words, height=self.height, width=self.width, bg=self.bg, fg=self.fg)
        self.but.place(x=self.x, y=self.y)

# Placeholder for window location
window = None

session_screen = tk.Frame(window, bg=bg_col)
session_screen.pack(expand=True, fill="both")

# Importing an image for background use
pic = tk.PhotoImage(file="Rectangle 1.png")

title = tk.Label(session_screen, text="Currently airing", font=(font_name, 30), bg=bg_col, fg=btn_col)
title.place(x=55, y=44)

movie_one = tk.Label(session_screen, image=pic, bg=bg_col)
movie_one.place(x=45, y=109)


# fix button stuff
buttt = session_button(movie_one, "hello", 20, 20, bg=btn_col, fg="red", x=233, y=0)
print(buttt.words)