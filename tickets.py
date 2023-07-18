import tkinter as tk

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

# Creating datetime variables
import datetime
dt = datetime.datetime.now()
first = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n1:00pm"
second = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n2:00pm"
third = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n3:00pm"

# Reading text file to get selected seat amount
seat_data = open("seat_data.txt", "r")
all_lines = seat_data.readlines()
seat_data.close()

seats = int(all_lines[1])

costs = {"adult": 10, "child": 7.5, "student": 9, "pensioner": 7}

tot = 5
adt_tickets = 0
chd_tickets = 0
stdn_tickets = 0
psr_tickets = 0


def screen_back():
    tickets.pack_forget()
    import seats as se
    se.seats.pack(expand=True, fill="both")

def screen_forward():
    tickets.pack_forget()
    import contact as ct
    ct.contact.pack(expand=True, fill="both")

    # Displays selected movie title on next page
    if "Spider" in movie_title.cget("text"):
        ct.movie_title.config(text="Spider-Man: Across the Spider-Verse")
        ct.image.config(image=spider)

    elif "Barbie" in movie_title.cget("text"):
        ct.movie_title.config(text="Barbie")
        ct.image.config(image=barbie)

    else:
        ct.movie_title.config(text="The Super Mario Bros. Movie")
        ct.image.config(image=mario)

    # Displays time of selected session 
    if time_label.cget("text") == first:
        ct.time_label.config(text=first)
    elif time_label.cget("text") == second:
        ct.time_label.config(text=second)
    else:
        ct.time_label.config(text="hello")


# fix


class place:
    # Widget placing class shorthand
    def __init__(self, widget, x, y):
        self.widget = widget
        self.x = x
        self.y = y
        self.widget.place(relx=self.x, rely=self.y, anchor="center")

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
                             fg=self.fg, command= self.comm, height = 2,
                             width=3, borderwidth=0,
                             highlightbackground=bg_col,
                             font=(font_name, 16))
        self.but.place(relx = self.x, rely = self.y, anchor = "center")





class seat_type():

    def test(self):
        print("hello")
        self.lab.config(text="hello")


    def increase(self):
        print(self.total_seats)
        if self.total_seats > 0 and self.type_of_ticket <= 60:
            self.total_seats -= 1
            print(self.total_seats)
            self.type_of_ticket += 1
        else:
            print("UR DUMB")

        self.lab.config(text=self.type_of_ticket)
        seat_amt['text'] = f"Seats selected: {self.total_seats}"

        return self.total_seats, self.type_of_ticket


    def decrease(self):
        if self.type_of_ticket > 0 and self.type_of_ticket <= self.total_seats:
            self.type_of_ticket -= 1
            self.total_seats += 1
        else:
            print("UR DUMB")

        self.lab.config(text=self.type_of_ticket)
        seat_amt["text"] = f"Seats selected: {self.total_seats}"

        return self.total_seats, self.type_of_ticket

    def __init__(self, location, type_of_ticket, total_seats = seats):
        self.location = location
        self.type_of_ticket = type_of_ticket
        self.total_seats = total_seats
        print(self.type_of_ticket)
        self.decr = create_button(self.location, "-", fg_col, btn_col, 0.7, 0.5, self.decrease)
        self.lab = tk.Label(self.location, text=self.type_of_ticket, fg=fg_col, bg="white", height=2,
                            width=3)
        place(self.lab, 0.8, 0.5)
        self.incr = create_button(self.location, "+", fg_col, btn_col, 0.9, 0.5, self.increase)



# Creating and configuring root window settings
window = None
tickets = tk.Frame(window, bg=bg_col, cursor="heart")


# Specified movie and session time
movie_title = tk.Label(tickets, text=None, font=(font_name, 30), fg=btn_col, bg=bg_col,
                       wraplength=200, justify="center")

time_label = tk.Label(tickets, text=None, justify="center", font=(font_name, 25),
                      fg=btn_col, bg=bg_col)
place(time_label, 0.1, 0.675)

image = tk.Label(tickets, image=None, bg=bg_col)
place(image, 0.1, 0.3)


# Page widgets

title_label = tk.Label(tickets, text="Tickets", font=(font_name, 40), fg=btn_col, bg=bg_col)
place(title_label, 0.5, 0.075)

fra = tk.Label(tickets, image=widget_bg, bg=bg_col)
place(fra, 0.6, 0.55)

seat_amt = tk.Label(fra, font=(font_name, 25), fg=btn_col, bg=img_bg)
place(seat_amt, 0.5, 0.1)


# Seat type labels
adult = tk.Label(fra, image=type_bg, bg=img_bg)
place(adult, 0.5, 0.2)
adt_info = tk.Label(adult, text="Adult \t ${:.2f}".format(costs["adult"]), fg=fg_col, bg=btn_col,
                    font=(font_name, 30))
place(adt_info, 0.3, 0.5)

child = tk.Label(fra, image=type_bg, bg=img_bg)
place(child, 0.5, 0.4)
chd_info = tk.Label(child, text="Child \t ${:.2f}".format(costs["child"]), fg=fg_col, bg=btn_col,
                    font=(font_name, 30))
place(chd_info, 0.3, 0.5)

student = tk.Label(fra, image=type_bg, bg=img_bg)
place(student, 0.5, 0.6)
stdn_info = tk.Label(student, text="Student \t ${:.2f}".format(costs["student"]), fg=fg_col, bg=btn_col,
                    font=(font_name, 30))
place(stdn_info, 0.3, 0.5)

pensioner = tk.Label(fra, image=type_bg, bg=img_bg)
place(pensioner, 0.5, 0.8)
psr_info = tk.Label(pensioner, text="Pensioner \t ${:.2f}".format(costs["pensioner"]), fg=fg_col, bg=btn_col,
                    font=(font_name, 30))
place(psr_info, 0.3, 0.5)


adt = seat_type(adult, adt_tickets)
chd = seat_type(child, chd_tickets)
stdn = seat_type(student, stdn_tickets)
psr = seat_type(pensioner, psr_tickets)


# find way to save ticket amounts


# Page controlling buttons
back = create_button(fra, "Back", fg_col, btn_col, 0.15, 0.95, comm=screen_back)
forward = create_button(fra, "Confirm", fg_col, btn_col, 0.85, 0.95, screen_forward)