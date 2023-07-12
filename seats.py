import tkinter as tk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

# Importing image
img = tk.PhotoImage(file="img.png")

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

class create_button:

    def __init__(self, location, text, fg, bg, x, y):
        self.location = location
        self.text = text
        self.fg = fg
        self.bg = bg
        self.x = x
        self.y = y
        self.but = tk.Button(self.location, bg = self.bg, text = self.text,
                             fg=bg_col, command= None, height = 1,
                             borderwidth=0, font=(font_name, ))
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

window = None

# Creating and configuring root window settings
seats = tk.Frame(window, bg=bg_col)
seats.pack(expand=True, fill="both")

# Creating overall frame's widgets
image = tk.Label(seats, image=img, bg=bg_col)
image.place(relx=0.1, rely=0.15, anchor="center")

movie_title = tk.Label(seats, text="Movie One", font=(font_name, 40), fg=btn_col, bg=bg_col)
movie_title.place(relx=0.3, rely=0.1, anchor="center")

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
session_label = tk.Label(seats, text = "Session\nTime", justify="center", font=(font_name, 30),
                         fg=btn_col, bg=bg_col)
session_label.place(relx=0.1, rely=0.35, anchor="center")
# get the session pressed from previous screen


# Page controlling buttons
back = create_button(seats, "Back", bg_col, btn_col, 0.4, 0.95,)


# Second frame containing seats
seat_container = tk.Frame(seats, height=400, width=750, relief="flat",
                          bg=img_bg, cursor="heart", bd=5)
seat_container.place(relx=0.2, rely=0.3)