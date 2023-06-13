import tkinter as tk

# Constant
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
font_name = "Yu Gothic Ui Semilight"

# Placeholder for window location
window = None

session_screen = tk.Frame(window, bg=bg_col)
session_screen.pack(expand=True, fill="both")

but = tk.Button(session_screen, text="hello")
but.pack()