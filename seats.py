import tkinter as tk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

# Importing image
img = tk.PhotoImage(file="img.png")

class create_button:

    def __init__(self, location, fg, x, y, state = "normal"):
        self.location = location
        self.fg = fg
        self.x = x
        self.y = y
        self.state = state
        self.but = tk.Button(self.location, fg = self.fg,
                             state=self.state, height = 1, command=None,
                             borderwidth=0)
        self.but.place(relx = self.x, rely = self.y, anchor = "center")

window = None

# Creating and configuring root window settings

seats_screen = tk.Frame(window, bg=bg_col)
seats_screen.pack(expand=True, fill="both")

# Creating overall frame's widgets
image = tk.Label(window, image=img, bg=bg_col)
image.place(relx=0.1, rely=0.15, anchor="center")

movie_title = tk.Label(window, text="Movie One", font=(font_name, 40), fg=btn_col, bg=bg_col)
movie_title.place(relx=0.3, rely=0.1, anchor="center")

# Availability labels
selected = tk.Label(window, text="Selected", font=(font_name, 25), fg=btn_col, bg=bg_col)
selected.place(relx=0.3, rely=0.2, anchor="center")
selected_box = create_button(window, "green", 0.25, 0.2, "disabled")

booked = tk.Label(window, text="Booked", font=(font_name, 25), fg=btn_col, bg=bg_col)
booked.place(relx=0.5, rely=0.2, anchor="center")

disability = tk.Label(window, text="Disability", font=(font_name, 25), fg=btn_col, bg=bg_col)
disability.place(relx=0.7, rely=0.2, anchor="center")

available = tk.Label(window, text="Available", font=(font_name, 25), fg=btn_col, bg=bg_col)
available.place(relx=0.9, rely=0.2, anchor="center")

test = tk.Label(window, fg="green", bg="green", height=10)
test.place(relx=0.5, rely=0.5)