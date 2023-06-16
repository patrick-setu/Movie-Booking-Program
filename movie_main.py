# Importing modules/tinker
import tkinter as tk
from tkinter import font


# Creating and setting tinker settings
window = tk.Tk()
window.title("Movie Booking Program")
window.geometry("996x700")
# window.config(bg="#EEF4ED")
window.resizable(False, False)


# Creating short-hand for widget settings
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
font_name = "Yu Gothic Ui Semilight"

# Importing files here for no error
# import start as st
# st.window = window

import session_picker as sp
sp.window = window



window.mainloop()
