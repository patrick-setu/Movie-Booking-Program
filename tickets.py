"""Import tkinter for GUI."""
import tkinter as tk
import datetime

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

widget_bg = tk.PhotoImage(file="ticket_rect.png")
type_bg = tk.PhotoImage(file="type_rect.png")

# Importing images
bimg = tk.PhotoImage(file="rect.png")
spider = tk.PhotoImage(file="spider 1.png")
barbie = tk.PhotoImage(file="barbie.png")
mario = tk.PhotoImage(file="mario.png")

dt = datetime.datetime.now()
first = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n1:00pm"
second = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n2:00pm"
third = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n3:00pm"

costs = {"adult": 10, "child": 7.5, "student": 9, "pensioner": 7}

tot = 0
adt_tickets = 0
chd_tickets = 0
stdn_tickets = 0
psr_tickets = 0


read = open("seat_data.txt", "r")
read_all = read.readlines()
read.close()



def screen_back():
    """Return to previous screen."""
    global tot
    tickets.pack_forget()
    import seats as se

    se.seats.pack(expand=True, fill="both")


def screen_forward():
    """Proceed to next screen."""
    tickets.pack_forget()
    import contact as ct
        
    ct.contact.pack(expand=True, fill="both")

    # Displays selected movie title on next page
    if "Spider" in movie_title.cget("text"):
        ct.movie_title.config(
            text="Spider-Man: Across the Spider-Verse",
            wraplength=200,
            font=(font_name, 14),
        )
        ct.image.config(image=spider)

    elif "Barbie" in movie_title.cget("text"):
        ct.movie_title.config(text="Barbie")
        ct.image.config(image=barbie)

    else:
        ct.movie_title.config(text="The Super Mario Bros. Movie")
        ct.image.config(image=mario)

    # Displays time of selected session
    ct.time_label["text"] = time_label["text"]

    # Updates into text file:
    stored_data = open("seat_data.txt", "r")
    data = stored_data.readlines()
    stored_data.close()

    stored_data = open("seat_data.txt", 'w')
    stored_data_copied = open("seat_data_copy.txt", 'r')
    copied_data = stored_data_copied.readlines()

    if len(data) > 4:
        while True:
            if len(data) == 4:
                break
            data.pop(-1)

    if len(data) == 4:
        for each_copied_data in copied_data:
            stored_data.write(each_copied_data)
        stored_data.write(
        "x{} Adult    \t${:.2f}\n".format(seats.adults, (seats.adults * costs["adult"]))
        )
        stored_data.write(
        "x{} Child    \t${:.2f}\n".format(seats.child, (seats.child * costs["child"]))
        )
        stored_data.write(
        "x{} Student \t${:.2f}\n".format(
            seats.student, (seats.student * costs["student"])
        )
        )
        stored_data.write(
        "x{} Pensioner \t${:.2f}\n".format(
            seats.pensioner, (seats.pensioner * costs["pensioner"])
        )
        )
        stored_data.write(
        "Total: ${:.2f}\n\n".format(
            (seats.adults * costs["adult"])
            + (seats.child * costs["child"])
            + (seats.student * costs["student"])
            + (seats.pensioner * costs["pensioner"])
        )
        )
        stored_data.close()



    txt = open("seat_data.txt", "r")
    sum_text = txt.readlines()
    txt.close()

    a = sum_text[4]
    c = sum_text[5]
    s = sum_text[6]
    p = sum_text[7]
    t = sum_text[8]

    display_sum = f"{a}{c}{s}{p}"
    ct.show_summary["text"] = display_sum
    ct.total["text"] = t


class Place:
    """Widget placing class shorthand."""

    def __init__(self, widget, x, y):
        """Place widget based on x, y."""
        self.widget = widget
        self.x = x
        self.y = y
        self.widget.place(relx=self.x, rely=self.y, anchor="center")


class CreateButton:
    """Create instance of a button."""

    def __init__(self, location, text, fg, bg, x, y, comm=None, stater = "normal"):
        """Take input to stylise button."""
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
            state = stater,
            height=1,
            width=7,
            borderwidth=0,
            highlightbackground=bg_col,
            font=(font_name, 16),
        )
        self.but.place(relx=self.x, rely=self.y, anchor="center")


class SeatType:
    """Class which makes the ticket amount buttons and label."""

    def incerease(self, counter, id):
        if id == "adult":
            self.adults += 1
            counter['text'] = self.adults
            if self.adults > 0:
                self.decr_1["state"] = 'normal'
        elif id == "child":
            self.child += 1
            counter['text'] = self.child
            if self.child > 0:
                self.decr_2["state"] = 'normal'
        elif id == 'student':
            self.student += 1
            counter['text'] = self.student
            if self.student > 0:
                self.decr_3["state"] = 'normal'
        elif id == 'pensioner':
            self.pensioner += 1
            counter['text'] = self.pensioner
            if self.pensioner > 0:
                self.decr_4["state"] = 'normal'

        self.type_of_ticket += 1
        if self.type_of_ticket == tot:
            self.incr_1["state"] = 'disabled'
            self.incr_2["state"] = 'disabled'
            self.incr_3["state"] = 'disabled'
            self.incr_4["state"] = 'disabled'
            forward.but['state'] = 'normal'
        elif self.type_of_ticket < tot:
            self.incr_1["state"] = 'normal'
            self.incr_2["state"] = 'normal'
            self.incr_3["state"] = 'normal'
            self.incr_4["state"] = 'normal'
            forward.but['state'] = 'disabled'

    def decrese(self, counter, id):
        
        if id == 'adult':
            if self.adults <= 0:
                self.decr_1["state"] = 'disabled'
            else:
                self.adults -= 1
                counter['text'] = self.adults
                if self.adults <= 0:
                    self.decr_1["state"] = 'disabled'


        elif id == 'child':
            if self.child <= 0:
                self.decr_2["state"] = 'disabled'
            else:
                self.child -= 1
                counter['text'] = self.child
                if self.child <= 0:
                    self.decr_2["state"] = 'disabled'


        elif id == 'student':
            if self.student <= 0:
                self.decr_3["state"] = 'disabled'
            else:
                self.student -= 1
                counter['text'] = self.student
                if self.student <= 0:
                    self.decr_3["state"] = 'disabled'

        elif id == 'pensioner':
            if self.pensioner <= 0:
                self.decr_4["state"] = 'disabled'
            else:
                self.pensioner -= 1
                counter['text'] = self.pensioner
                if self.pensioner <= 0:
                    self.decr_4["state"] = 'disabled'

        self.type_of_ticket -= 1
        if self.type_of_ticket < tot:
            self.incr_1["state"] = 'normal'
            self.incr_2["state"] = 'normal'
            self.incr_3["state"] = 'normal'
            self.incr_4["state"] = 'normal'
            forward.but['state'] = 'disabled'



    def __init__(self):
        """Create instances of ticket controlling buttons."""
        self.type_of_ticket = 0
        self.adults = 0
        self.child = 0
        self.student = 0
        self.pensioner = 0


        self.lab_1 = tk.Label(
            adult,
            text=self.type_of_ticket,
            fg=fg_col,
            bg="white",
            height=2,
            width=3,
            font=(font_name, 16),
        )
        self.lab_1.place(relx=0.8, rely=0.5, anchor="center")

        self.lab_2 = tk.Label(
            child,
            text=self.type_of_ticket,
            fg=fg_col,
            bg="white",
            height=2,
            width=3,
            font=(font_name, 16),
        )
        self.lab_2.place(relx=0.8, rely=0.5, anchor="center")

        self.lab_3 = tk.Label(
            student,
            text=self.type_of_ticket,
            fg=fg_col,
            bg="white",
            height=2,
            width=3,
            font=(font_name, 16),
        )
        self.lab_3.place(relx=0.8, rely=0.5, anchor="center")

        self.lab_4 = tk.Label(
            pensioner,
            text=self.type_of_ticket,
            fg=fg_col,
            bg="white",
            height=2,
            width=3,
            font=(font_name, 16)
        )
        self.lab_4.place(relx=0.8, rely=0.5, anchor="center")

        self.decr_1 = tk.Button(
            adult,
            text="-",
            fg=fg_col,
            bg=btn_col,
            command= lambda: self.decrese(self.lab_1, "adult"),
            state = 'disabled',
            height=2,
            width=3,
        )
        self.decr_1.place(relx=0.7, rely=0.5, anchor="center")

        self.decr_2 = tk.Button(
            child,
            text="-",
            fg=fg_col,
            bg=btn_col,
            command=lambda: self.decrese(self.lab_2, "child"),
            state = 'disabled',
            height=2,
            width=3,
        )
        self.decr_2.place(relx=0.7, rely=0.5, anchor="center")

        self.decr_3 = tk.Button(
            student,
            text="-",
            fg=fg_col,
            bg=btn_col,
            command=lambda: self.decrese(self.lab_3, "student"),
            state = 'disabled',
            height=2,
            width=3,
        )
        self.decr_3.place(relx=0.7, rely=0.5, anchor="center")

        self.decr_4 = tk.Button(
            pensioner,
            text="-",
            fg=fg_col,
            bg=btn_col,
            command=lambda: self.decrese(self.lab_4, "pensioner"),
            state = 'disabled',
            height=2,
            width=3,
        )
        self.decr_4.place(relx=0.7, rely=0.5, anchor="center")

        self.incr_1 = tk.Button(
            adult,
            text="+",
            fg=fg_col,
            bg=btn_col,
            command = lambda: self.incerease(self.lab_1, 'adult'),
            height=2,
            width=3
        )
        self.incr_1.place(relx=0.9, rely=0.5, anchor="center")

        self.incr_2 = tk.Button(
            child,
            text="+",
            fg=fg_col,
            bg=btn_col,
            command = lambda: self.incerease(self.lab_2, "child"),
            height=2,
            width=3
        )
        self.incr_2.place(relx=0.9, rely=0.5, anchor="center")

        self.incr_3 = tk.Button(
            student,
            text="+",
            fg=fg_col,
            bg=btn_col,
            command = lambda: self.incerease(self.lab_3, "student"),
            height=2,
            width=3
        )
        self.incr_3.place(relx=0.9, rely=0.5, anchor="center")

        self.incr_4 = tk.Button(
            pensioner,
            text="+",
            fg=fg_col,
            bg=btn_col,
            command = lambda: self.incerease(self.lab_4, "pensioner"),
            height=2,
            width=3
        )
        self.incr_4.place(relx=0.9, rely=0.5, anchor="center")


# Creating and configuring root window settings
window = None
tickets = tk.Frame(window, bg=bg_col)


# Specified movie and session time
movie_title = tk.Label(
    tickets,
    text=None,
    font=(font_name, 20),
    fg=btn_col,
    bg=bg_col,
    wraplength=180,
    justify="center",
)
Place(movie_title, 0.15, 0.5)

time_label = tk.Label(
    tickets, text=None, justify="center", font=(font_name, 20), fg=btn_col, bg=bg_col
)
Place(time_label, 0.15, 0.7)

image = tk.Label(tickets, image=None, bg=bg_col)
Place(image, 0.15, 0.3)


# Page widgets

title_label = tk.Label(
    tickets, text="Tickets", font=(font_name, 30), fg=btn_col, bg=bg_col
)
Place(title_label, 0.5, 0.075)

fra = tk.Label(tickets, image=widget_bg, bg=bg_col)
Place(fra, 0.6, 0.55)

seat_amt = tk.Label(fra, font=(font_name, 25), fg=btn_col, bg=img_bg)
Place(seat_amt, 0.5, 0.1)


# Seat type labels
adult = tk.Label(fra, image=type_bg, bg=img_bg)
Place(adult, 0.5, 0.2)
adt_info = tk.Label(
    adult,
    text="Adult \t ${:.2f}".format(costs["adult"]),
    fg=fg_col,
    bg=btn_col,
    font=(font_name, 20),
)
Place(adt_info, 0.3, 0.5)

child = tk.Label(fra, image=type_bg, bg=img_bg)
Place(child, 0.5, 0.4)
chd_info = tk.Label(
    child,
    text="Child \t ${:.2f}".format(costs["child"]),
    fg=fg_col,
    bg=btn_col,
    font=(font_name, 20),
)
Place(chd_info, 0.3, 0.5)

student = tk.Label(fra, image=type_bg, bg=img_bg)
Place(student, 0.5, 0.6)
stdn_info = tk.Label(
    student,
    text="Student \t ${:.2f}".format(costs["student"]),
    fg=fg_col,
    bg=btn_col,
    font=(font_name, 20),
)
Place(stdn_info, 0.3, 0.5)

pensioner = tk.Label(fra, image=type_bg, bg=img_bg)
Place(pensioner, 0.5, 0.8)
psr_info = tk.Label(
    pensioner,
    text="Pensioner  ${:.2f}".format(costs["pensioner"]),
    fg=fg_col,
    bg=btn_col,
    font=(font_name, 20),
)
Place(psr_info, 0.3, 0.5)



# find way to save ticket amounts


# Page controlling buttons
back = CreateButton(fra, "Back", fg_col, btn_col, 0.15, 0.95, screen_back)
forward = CreateButton(fra, "Confirm", fg_col, btn_col, 0.85, 0.95, screen_forward, 'disabled')


seats = SeatType()

