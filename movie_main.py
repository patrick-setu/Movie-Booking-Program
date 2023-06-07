# Importing modules/tinker
import tkinter as tk
from tkinter import font
import sys


# Creating and setting tinker settings
window = tk.Tk()
window.title("Movie Booking Program")
window.geometry("996x700")
window.config(bg="#EEF4ED")


# Creating short-hand for widget settings
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
font_name = "Yu Gothic Ui Semilight"


# Listing definitions

def close_btn():
    sys.exit()




# Creates frame and widgets for first page
start_screen = tk.Frame(window, bg=bg_col)
start_screen.pack(expand=True, fill="both")

name_label = tk.Label(start_screen , text="Patrick Cinema", font=(font_name, 60), bg=bg_col, fg=btn_col)
name_label.place(x = 251, y = 184)

book_btn = tk.Button(start_screen, text="Session Times", font=(font_name, 30), bg=btn_col, fg=bg_col)
book_btn.place(x=353, y=321)

exit_btn = tk.Button(start_screen, text="Exit", font=(font_name, 30), bg=btn_col, fg=bg_col, command=close_btn)
exit_btn.place(x=443, y=445)





# pic = tk.PhotoImage(file="Rectangle 1.png")

# piclab = tk.Label(start_screen, image=pic, )
# piclab.pack()

window.mainloop()
