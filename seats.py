import tkinter as tk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"


class seat_label:

    def __init__(self, location, bg, x, y,):
        self.location = location
        self.bg = bg
        self.x = x
        self.y = y
        self.but = tk.Button(self.location, bg = self.bg,
                             state="disabled", height = 1,
                             borderwidth=0)
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

def screen_back():
    seats.pack_forget()
    import sessions as ss
    ss.session_screen.pack(expand=True, fill="both")

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
                             fg=bg_col, command= self.comm, height = 1,
                             borderwidth=0, highlightbackground=bg_col)
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

window = None

# Creating and configuring root window settings
seats = tk.Frame(window, bg=bg_col)
seats.pack(expand=True, fill="both")

# Creating overall frame's widgets
image = tk.Label(seats, image=None, bg=bg_col)
image.place(relx=0.1, rely=0.15, anchor="center")

movie_title = tk.Label(seats, text=None, font=(font_name, 40), fg=btn_col, bg=bg_col)

# Availability labels
selected = tk.Label(seats, text="Selected", font=(font_name, 25), fg=btn_col, bg=bg_col)
selected.place(relx=0.3, rely=0.2, anchor="center")
selected_box = seat_label(seats, "green", 0.23, 0.2)

booked = tk.Label(seats, text="Booked", font=(font_name, 25), fg=btn_col, bg=bg_col)
booked.place(relx=0.5, rely=0.2, anchor="center")
booked_box = seat_label(seats, "red", 0.43, 0.2)

disability = tk.Label(seats, text="Disability", font=(font_name, 25), fg=btn_col, bg=bg_col)
disability.place(relx=0.7, rely=0.2, anchor="center")
disability_box = seat_label(seats, "yellow", 0.63, 0.2)

available = tk.Label(seats, text="Available", font=(font_name, 25), fg=btn_col, bg=bg_col)
available.place(relx=0.9, rely=0.2, anchor="center")
available_box = seat_label(seats, "white", 0.83, 0.2)

# Specified movie and session time
session_label = tk.Label(seats, text = "Session", justify="center", font=(font_name, 40),
                         fg=btn_col, bg=bg_col)
session_label.place(relx=0.1, rely=0.325, anchor="center")

time_label = tk.Label(seats, text=None, justify="center", font=(font_name, 25),
                      fg=btn_col, bg=bg_col)
time_label.place(relx=0.1, rely=0.45, anchor="center")


# Page controlling buttons
back = create_button(seats, "Back", bg_col, btn_col, 0.4, 0.95, comm=screen_back)


# Second frame containing seats
seat_container = tk.Frame(seats, height=400, width=750, relief="flat",
                          bg=img_bg, cursor="heart", bd=5)
seat_container.place(relx=0.2, rely=0.3)

hi = tk.Label(seat_container, text="hello", fg = "red", bg="white")
hi.grid(row = 0, column=2)

r=60
rw = 1
clm = 1
for i in range(r):
    test = tk.Button(seat_container, fg="green", height=1, padx= 5, pady=5)
    test.grid(row=(0+rw), column=(0+clm), padx=8, pady=7)
    test.grid_propagate(False)
    rw += 1
    if rw == 6:
        rw = 0
        clm += 1

