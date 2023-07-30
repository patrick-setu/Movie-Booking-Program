"""Import tkinter for GUI."""
import tkinter as tk
from tkinter import messagebox
import random as r
import datetime

# editing this one to pep8

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

# Importing images
bimg = tk.PhotoImage(file="rect.png")
spider = tk.PhotoImage(file="spider 1.png")
barbie = tk.PhotoImage(file="barbie.png")
mario = tk.PhotoImage(file="mario.png")

# Creating datetime variables
dt = datetime.datetime.now()
first = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n\n1:00pm"
second = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n\n2:00pm"
third = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n\n3:00pm"


class SeatLabel:
    """Show keys for different seat availabilities."""

    def __init__(
        self,
        location,
        bg,
        x,
        y,
    ):
        """Create an instance of a seat label."""
        self.location = location
        self.bg = bg
        self.x = x
        self.y = y
        self.but = tk.Button(
            self.location,
            bg=self.bg,
            state="disabled",
            height=1,
            borderwidth=0,
            padx=5,
            pady=5,
        )
        self.but.place(relx=self.x, rely=self.y, anchor="center")


def screen_back():
    """Go back to previous screen."""
    seats.pack_forget()
    import sessions as ss

    ss.session_screen.pack(expand=True, fill="both")


def screen_forward():
    """Proceed to next page if at least 1 seat selected."""
    if len(selected_seats) < 1:
        messagebox.showerror("Error", "No seats have been selected")
    else:
        selected_seats.sort()
        stored_seats = open("seat_data.txt", "w")
        stored_seats.write("Amount of selected seats:\n")
        stored_seats.write(f"{len(selected_seats)}\n")
        stored_seats.write(f"Selected seats:\n{selected_seats}\n")
        stored_seats.close()

        seats.pack_forget()
        import tickets as ts

        ts.tickets.pack(expand=True, fill="both")

        seat_data = open("seat_data.txt", "r")
        all_lines = seat_data.readlines()
        seat_data.close()

        ts.seat_amt["text"] = f"Seats selected: {all_lines[1]}"

        # Displays selected movie title on next page
        if "Spider" in movie_title.cget("text"):
            ts.movie_title.config(text="Spider-Man: Across the Spider-Verse")
            ts.image.config(image=spider)

        elif "Barbie" in movie_title.cget("text"):
            ts.movie_title.config(text="Barbie")
            ts.image.config(image=barbie)

        elif "Mario" in movie_title.cget("text"):
            ts.movie_title.config(text="The Super Mario Bros. Movie")
            ts.image.config(image=mario)

        # Displays time of selected session
        ts.time_label["text"] = time_label["text"]

        # Lets each ticket type know the max value/selected seat amount
        ts.adt.total_seats = int(all_lines[1])
        ts.chd.total_seats = int(all_lines[1])
        ts.stdn.total_seats = int(all_lines[1])
        ts.psr.total_seats = int(all_lines[1])


def pop_up():
    """Create help popup."""
    help = tk.Toplevel(window, bg=bg_col)
    help.geometry("600x400")
    help.title("Seat selection help")
    help.resizable(False, False)

    help_bg = tk.Frame(help, bg=img_bg, height=350, width=450)
    help_bg.place(relx=0.5, rely=0.5, anchor="center")

    title = tk.Label(
        help_bg,
        text="Seat selection help",
        fg=btn_col,
        background=img_bg,
        font=(font_name, 25),
    )
    title.place(relx=0.5, rely=0.2, anchor="center")

    body_text = tk.Label(
        help_bg,
        text="Click to select seats\n"
        "(Maximum of 60 unless reserved)\n\n"
        "Please check availability keys\n"
        "then press confirm when done or press the back button",
        wraplength=300,
        fg=btn_col,
        bg=img_bg,
        font=(font_name, 15),
        justify="center",
    )
    body_text.place(relx=0.5, rely=0.5, anchor="center")

    help.grab_set()
    CreateButton(help_bg, "Close", fg_col, btn_col, 0.5, 0.9, lambda: help.destroy())


class CreateButton:
    """Create instance of a button."""

    def __init__(self, location, text, fg, bg, x, y, comm=None):
        """Take several inputted arguments to stylise."""
        self.location = location
        self.text = text
        self.fg = fg
        self.bg = bg
        self.x = x
        self.y = y
        self.comm = comm
        self.but = tk.Button(
            self.location,
            bg=self.bg,
            text=self.text,
            fg=self.fg,
            command=self.comm,
            height=1,
            width=7,
            borderwidth=0,
            highlightbackground=bg_col,
            font=(font_name, 16),
        )
        self.but.place(relx=self.x, rely=self.y, anchor="center")


# Creating and configuring root window settings
window = None
seats = tk.Frame(window, bg=bg_col)

# Creating overall frame's widgets
image = tk.Label(seats, image=None, bg=bg_col)
image.place(relx=0.1, rely=0.15, anchor="center")

movie_title = tk.Label(seats, text=None, font=(font_name, 30), fg=btn_col, bg=bg_col)

screen_label = tk.Label(
    seats, text="Seats", fg=btn_col, bg=bg_col, font=(font_name, 25)
)
screen_label.place(relx=0.6, rely=0.25, anchor="center")

# Availability labels
selected = tk.Label(seats, text="Selected", font=(font_name, 25), fg=btn_col, bg=bg_col)
selected.place(relx=0.3, rely=0.175, anchor="center")
selected_box = SeatLabel(seats, "green", 0.23, 0.175)

booked = tk.Label(seats, text="Booked", font=(font_name, 25), fg=btn_col, bg=bg_col)
booked.place(relx=0.5, rely=0.175, anchor="center")
booked_box = SeatLabel(seats, "red", 0.43, 0.175)

disability = tk.Label(
    seats, text="Disability", font=(font_name, 25), fg=btn_col, bg=bg_col
)
disability.place(relx=0.7, rely=0.175, anchor="center")
disability_box = SeatLabel(seats, "yellow", 0.63, 0.175)

available = tk.Label(
    seats, text="Available", font=(font_name, 25), fg=btn_col, bg=bg_col
)
available.place(relx=0.9, rely=0.175, anchor="center")
available_box = SeatLabel(seats, "white", 0.83, 0.175)

# Specified movie and session time
session_label = tk.Label(
    seats,
    text="Session:",
    justify="center",
    font=(font_name, 30),
    fg=btn_col,
    bg=bg_col,
)
session_label.place(relx=0.1, rely=0.325, anchor="center")

time_label = tk.Label(
    seats, text=None, justify="center", font=(font_name, 25), fg=btn_col, bg=bg_col
)
time_label.place(relx=0.1, rely=0.5, anchor="center")

# Second frame containing seats
seat_container = tk.Frame(seats, height=400, width=750, relief="flat", bg=img_bg, bd=5)
seat_container.place(relx=0.2, rely=0.3)

selected_seats = []


class SeatMaker:
    """Change button colour based on seat IntVar."""

    def seat_clicked(self, seat_state, seat):
        """Store user seat data"""
        seat_position = seat.grid_info()
        letter = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
        k = list(letter.keys())
        v = list(letter.values())
        pos = v.index(seat_position["row"])
        lett = k[pos]

        # Program turns seat (un)selected based on state
        if seat_state.get() == 0:
            # Turning unselected into selected state
            seat_state.set(1)
        elif seat_state.get() == 1:
            # Turning selected into unselected state
            seat_state.set(0)
        elif seat_state.get() == 2:
            # Turning disabled unselected into selected state
            seat_state.set(3)
        else:
            # Turning disabled selected into unselected state
            seat_state.set(2)

        if seat_state.get() == 1:
            # Make selected when state is 1
            seat["bg"] = "green"
            selected_seats.append((str(lett) + str(seat_position["column"] + 1)))
        elif seat_state.get() == 0:
            # Make unselected when state is 0
            seat["bg"] = "white"
            selected_seats.pop()
        elif seat_state.get() == 3:
            # Make disabled seat selected when state is 2
            seat["bg"] = "green"
            selected_seats.append((str(lett) + str(seat_position["column"] + 1)))
        elif seat_state.get() == 2:
            # Make disabled seat unselected when state is 3
            seat["bg"] = "yellow"
            selected_seats.pop()

        selected["text"] = seat["bg"]

    def __init__(self, location, column):
        """Column value inputted to class.
        
        Create column of seats from value.
        """
        self.bg_1 = "white"
        self.bg_2 = "white"
        self.bg_3 = "white"
        self.bg_4 = "white"
        self.bg_5 = "white"
        self.width_seat = "4"
        self.height_seat = "2"
        self.seat_1_state = tk.IntVar()
        self.seat_2_state = tk.IntVar()
        self.seat_3_state = tk.IntVar()
        self.seat_4_state = tk.IntVar()
        self.seat_5_state = tk.IntVar()

        self.booked_seat_plac = r.randint(1, 6)
        if self.booked_seat_plac == 1:
            self.bg_1 = "red"
        elif self.booked_seat_plac == 2:
            self.bg_2 = "red"
        elif self.booked_seat_plac == 3:
            self.bg_3 = "red"
        elif self.booked_seat_plac == 4:
            self.bg_4 = "red"
        else:
            self.bg_5 = "red"

        self.seat_button_1 = tk.Button(
            location,
            background=self.bg_1,
            width=self.width_seat,
            height=self.height_seat,
            command=lambda: self.seat_clicked(self.seat_1_state, self.seat_button_1),
        )
        self.seat_button_1.grid(row=0, column=column, pady=12, padx=10)

        if self.seat_button_1["bg"] == "red":
            self.seat_button_1["state"] = "disabled"
        else:
            pass

        self.seat_button_2 = tk.Button(
            location,
            background=self.bg_2,
            width=self.width_seat,
            height=self.height_seat,
            command=lambda: self.seat_clicked(self.seat_2_state, self.seat_button_2),
        )
        self.seat_button_2.grid(row=1, column=column, pady=12, padx=10)

        if self.seat_button_2["bg"] == "red":
            self.seat_button_2["state"] = "disabled"
        else:
            pass

        self.seat_button_3 = tk.Button(
            location,
            background=self.bg_3,
            width=self.width_seat,
            height=self.height_seat,
            command=lambda: self.seat_clicked(self.seat_3_state, self.seat_button_3),
        )
        self.seat_button_3.grid(row=2, column=column, pady=12, padx=10)

        if self.seat_button_3["bg"] == "red":
            self.seat_button_3["state"] = "disabled"
        else:
            pass

        self.seat_button_4 = tk.Button(
            location,
            background=self.bg_4,
            width=self.width_seat,
            height=self.height_seat,
            command=lambda: self.seat_clicked(self.seat_4_state, self.seat_button_4),
        )
        self.seat_button_4.grid(row=3, column=column, pady=12, padx=10)

        if self.seat_button_4["bg"] == "red":
            self.seat_button_4["state"] = "disabled"
        else:
            pass

        self.seat_button_5 = tk.Button(
            location,
            background=self.bg_5,
            width=self.width_seat,
            height=self.height_seat,
            command=lambda: self.seat_clicked(self.seat_5_state, self.seat_button_5),
        )
        self.seat_button_5.grid(row=4, column=column, pady=12, padx=10)

        if self.seat_button_5["bg"] == "red":
            self.seat_button_5["state"] = "disabled"
        else:
            pass


# Creates 12 columns of 5 rows of seats
column_one_seats = SeatMaker(seat_container, 0)
column_two_seats = SeatMaker(seat_container, 1)
column_three_seats = SeatMaker(seat_container, 2)
column_four_seats = SeatMaker(seat_container, 3)
column_five_seats = SeatMaker(seat_container, 4)
column_six_seats = SeatMaker(seat_container, 5)
column_seven_seats = SeatMaker(seat_container, 6)
column_eight_seats = SeatMaker(seat_container, 7)
column_nine_seats = SeatMaker(seat_container, 8)
column_ten_seats = SeatMaker(seat_container, 9)
column_eleven_seats = SeatMaker(seat_container, 10)
column_twelve_seats = SeatMaker(seat_container, 11)

column_eleven_seats.seat_button_5["bg"] = "yellow"

# Setting disability chairs
# by getting column number and seat(row 1-5)
# column_one_seats.seat_5_state.set(2)
# column_one_seats.seat_button_5['bg'] = "yellow"
# column_two_seats.seat_5_state.set(2)
# column_two_seats.seat_button_5['bg'] = "yellow"
# column_three_seats.seat_5_state.set(2)
# column_three_seats.seat_button_5['bg'] = "yellow"
# column_ten_seats.seat_5_state.set(2)
# column_ten_seats.seat_button_5['bg'] = "yellow"
# column_eleven_seats.seat_5_state.set(2)
# column_eleven_seats.seat_button_5['bg'] = "yellow"
# column_twelve_seats.seat_5_state.set(2)
# column_twelve_seats.seat_button_5['bg'] = "yellow"

# Creates labels for rows and seat number
A_label = tk.Label(
    seat_container, text="A", font=(font_name, 24), background=img_bg, fg="white"
)
A_label.grid(row=0, column=12, sticky="NSWE", padx=2, pady=12)

B_label = tk.Label(
    seat_container, text="B", font=(font_name, 24), background=img_bg, fg="white"
)
B_label.grid(row=1, column=12, sticky="NSWE", padx=2, pady=12)

C_label = tk.Label(
    seat_container, text="C", font=(font_name, 24), background=img_bg, fg="white"
)
C_label.grid(row=2, column=12, sticky="NSWE", padx=2, pady=12)

D_label = tk.Label(
    seat_container, text="D", font=(font_name, 24), background=img_bg, fg="white"
)
D_label.grid(row=3, column=12, sticky="NSWE", padx=2, pady=12)

E_label = tk.Label(
    seat_container, text="E", font=(font_name, 24), background=img_bg, fg="white"
)
E_label.grid(row=4, column=12, sticky="NSWE", padx=2, pady=12)

label_1 = tk.Label(
    seat_container, text="1", font=(font_name, 24), background=img_bg, fg="white"
)
label_1.grid(row=8, column=0, sticky="NSWE", padx=2, pady=1)

label_2 = tk.Label(
    seat_container, text="2", font=(font_name, 24), background=img_bg, fg="white"
)
label_2.grid(row=8, column=1, sticky="NSWE", padx=2, pady=1)

label_3 = tk.Label(
    seat_container, text="3", font=(font_name, 24), background=img_bg, fg="white"
)
label_3.grid(row=8, column=2, sticky="NSWE", padx=2, pady=1)

label_4 = tk.Label(
    seat_container, text="4", font=(font_name, 24), background=img_bg, fg="white"
)
label_4.grid(row=8, column=3, sticky="NSWE", padx=2, pady=1)

label_5 = tk.Label(
    seat_container, text="5", font=(font_name, 24), background=img_bg, fg="white"
)
label_5.grid(row=8, column=4, sticky="NSWE", padx=2, pady=1)

label_6 = tk.Label(
    seat_container, text="6", font=(font_name, 24), background=img_bg, fg="white"
)
label_6.grid(row=8, column=5, sticky="NSWE", padx=2, pady=1)

label_7 = tk.Label(
    seat_container, text="7", font=(font_name, 24), background=img_bg, fg="white"
)
label_7.grid(row=8, column=6, sticky="NSWE", padx=2, pady=1)

label_8 = tk.Label(
    seat_container, text="8", font=(font_name, 24), background=img_bg, fg="white"
)
label_8.grid(row=8, column=7, sticky="NSWE", padx=2, pady=1)

label_9 = tk.Label(
    seat_container, text="9", font=(font_name, 24), background=img_bg, fg="white"
)
label_9.grid(row=8, column=8, sticky="NSWE", padx=2, pady=1)

label_10 = tk.Label(
    seat_container, text="10", font=(font_name, 24), background=img_bg, fg="white"
)
label_10.grid(row=8, column=9, sticky="NSWE", padx=2, pady=1)

label_11 = tk.Label(
    seat_container, text="11", font=(font_name, 24), background=img_bg, fg="white"
)
label_11.grid(row=8, column=10, sticky="NSWE", padx=2, pady=1)

label_12 = tk.Label(
    seat_container, text="12", font=(font_name, 24), background=img_bg, fg="white"
)
label_12.grid(row=8, column=11, sticky="NSWE", padx=2, pady=1)


# Page controlling buttons
back = CreateButton(seats, "Back", fg_col, btn_col, 0.4, 0.96, screen_back)
forward = CreateButton(seats, "Confirm", fg_col, btn_col, 0.6, 0.96, screen_forward)

top_help = CreateButton(seats, "Help?", img_bg, btn_col, 0.1, 0.96, pop_up)
