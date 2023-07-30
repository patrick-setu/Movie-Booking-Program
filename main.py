# Importing modules/tinker
"""Import tkinter for GUI."""
import tkinter as tk


# Creating and setting tinker settings
window = tk.Tk()
window.title("Movie Booking Program")
window.geometry("996x720")
window.config(bg="#EEF4ED")
# window.resizable(False, False) temporarily disabled


# Creating short-hand for widget settings
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
font_name = "Yu Gothic Ui Semilight"


import start as st


def change_frame1():
    """Change screen when clicked."""
    import sessions as ss
    ss.window = window
    st.start_screen.pack_forget()


st.window = window


st.book_btn.config(command=change_frame1)


window.mainloop()
