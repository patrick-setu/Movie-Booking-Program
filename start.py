import tkinter as tk

# Creating short-hand for widget settings

bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
font_name = "Yu Gothic Ui Semilight"

# Creates frame and widgets for first page

window = None

start_screen = tk.Frame(window, bg=bg_col)
start_screen.pack(expand=True, fill="both")

name_label = tk.Label(start_screen, text="Patrick Cinema", font=(font_name, 60), bg=bg_col, fg=btn_col)
name_label.place(relx=0.5, rely = 0.3,anchor="center")

book_btn = tk.Button(start_screen, text="Session Times", font=(font_name, 30), bg=btn_col,
 fg=bg_col)
book_btn.place(relx=0.5, rely = 0.5, anchor="center")

exit_btn = tk.Button(start_screen, text="Exit", font=(font_name, 30), bg=btn_col, fg=bg_col, command= lambda: window.destroy())
exit_btn.place(relx=0.5, rely = 0.7,anchor="center")
