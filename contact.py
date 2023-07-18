import tkinter as tk
from tkinter import ttk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

widget_bg = tk.PhotoImage(file="ticket_rect.png")
type_bg = tk.PhotoImage(file="type_rect.png")
ticket_bg = tk.PhotoImage(file="ticket_contact.png")

costs = {"adult": 10, "child": 7.5, "student": 9, "pensioner": 7}

# Creating and configuring root window settings
window = None
contact = tk.Frame(window, bg=bg_col, cursor="heart")

def screen_back():
    contact.pack_forget()
    import tickets as ts
    ts.tickets.pack(expand=True, fill="both")

class place:
    # Widget placing class shorthand
    def __init__(self, widget, x, y):
        self.widget = widget
        self.x = x
        self.y = y
        self.widget.place(relx=self.x, rely=self.y, anchor="center")

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
                             fg=self.fg, command= self.comm, height = 2,
                             width=5, borderwidth=0,
                             highlightbackground=bg_col,
                             font=(font_name, 16))
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

# Page widgets

display_bg = tk.Label(contact, image=ticket_bg, bg=bg_col, borderwidth=0)
place(display_bg, 0.5, 0.25)


# Specified movie and session time
image = tk.Label(display_bg)
place(image, 0.1, 0.3)
movie_title = tk.Label(display_bg, font=(font_name, 16), fg=btn_col, bg=img_bg,
                       wraplength=150, justify="center")
place(movie_title, 0.1, 0.7)
time_label = tk.Label(display_bg, justify="center", font=(font_name, 16),
                      fg=btn_col, bg=img_bg)
place(time_label, 0.1, 0.9)



show_summary = tk.Label(display_bg, text=None, width=40, fg=fg_col, bg=btn_col,
                        font=(font_name, 20), justify="left", state="disabled")
show_summary.place(relx=0.6, rely=0.55, anchor="center")



back = create_button(contact, "Back", fg_col, btn_col, 0.15, 0.95, comm=screen_back)