import tkinter as tk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"



def screen_back():
    tickets.pack_forget()
    import seats as se
    se.seats.pack(expand=True, fill="both")



class create_button:

    def __init__(self, location, text, fg, bg, x, y, comm = None):
        self.location = location
        self.text = text
        self.fg = fg
        self.bg = bg
        self.x = x
        self.y = y
        self.comm = comm
        self.but = tk.Button(self.location, bg = self.bg, text = self.text,
                             fg=bg_col, command= self.comm, height = 2,
                             width=3, borderwidth=0,
                             highlightbackground=bg_col)
        self.but.place(relx = self.x, rely = self.y, anchor = "center")



# Creating and configuring root window settings
window = None
tickets = tk.Frame(window, bg=bg_col)


back = create_button(tickets, "Back", bg_col, btn_col, 0.4, 0.95, comm=screen_back)