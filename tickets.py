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


costs = {"adult": 10, "child": 7.5, "student": 9, "pensioner": 7}

tot = 5
adt_tickets = 1
chd_tickets = 1
stdn_tickets = 1
psr_tickets = 1


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
    ct.time_label['text'] = time_label['text']

    # Updates into text file:
    # total cost, each ticket amount, each ticket type total
    stored_data = open("seat_data.txt", "a")
    stored_data.write("x{} Adult    \t${:.2f}\n".format(adt_tickets, (adt_tickets*costs['adult'])))
    stored_data.write("x{} Child    \t${:.2f}\n".format(chd_tickets, (chd_tickets*costs['child'])))
    stored_data.write("x{} Student \t${:.2f}\n".format(stdn_tickets, (stdn_tickets*costs['student'])))
    stored_data.write("x{} Pensioner \t${:.2f}\n".format(psr_tickets, (psr_tickets*costs['pensioner'])))
    stored_data.write("Total: ${:.2f}".format((adt_tickets*costs['adult'])+(chd_tickets*costs['child'])+(stdn_tickets*costs['student'])+(psr_tickets*costs['pensioner'])))
    stored_data.close()

    txt = open("seat_data.txt", "r")
    sum_text = txt.readlines()
    txt.close()

    print(sum_text)

    a = sum_text[4]
    c = sum_text[5]
    s = sum_text[6]
    p = sum_text[7]
    t = sum_text[8]

    display_sum = f"{a}{c}{s}{p}"
    ct.show_summary['text'] = display_sum
    ct.total['text'] = t

# fix


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
                             fg=self.fg, command= self.comm, height = 1,
                             width=7, borderwidth=0,
                             highlightbackground=bg_col,
                             font=(font_name, 16))
        self.but.place(relx = self.x, rely = self.y, anchor = "center")



class seat_type():
    # Class which makes the ticket amount buttons and label
    def increase(self):
        # Function to increase a ticket type but not exceed lower than selected amount
        print(self.total_seats)
        if self.total_seats > 0 and self.type_of_ticket <= 60:
            self.total_seats -= 1
            self.type_of_ticket += 1
        else:
            print("error")

        self.lab.config(text=self.type_of_ticket)

        # # return self.total_seats, self.type_of_ticket


    def decrease(self):
        # Function to decrease a ticket type but not exceed higher than selected amount
        if self.type_of_ticket > 0 and self.type_of_ticket <= self.total_seats:
            self.type_of_ticket -= 1
            self.total_seats += 1
        else:
            print("UR DUMB")

        self.lab.config(text=self.type_of_ticket)

        # return self.total_seats, self.type_of_ticket
        pass

    def __init__(self, location, type_of_ticket, total_seats):
        self.location = location
        self.type_of_ticket = type_of_ticket
        self.total_seats = total_seats
        self.decr = tk.Button(self.location, text="-", fg=fg_col, bg=btn_col, command=self.decrease,
                              height=2, width=3)
        self.decr.place(relx=0.7, rely=0.5, anchor="center")
        self.lab = tk.Label(self.location, text=self.type_of_ticket, fg=fg_col, bg="white", height=2,
                            width=3, font=(font_name, 16))
        self.lab.place(relx=0.8, rely=0.5, anchor="center")
        self.incr = tk.Button(self.location, text="+", fg=fg_col, bg=btn_col, command=self.increase,
                              height=2, width=3)
        self.incr.place(relx=0.9, rely=0.5, anchor="center")



# Creating and configuring root window settings
window = None
tickets = tk.Frame(window, bg=bg_col, cursor="heart")


# Specified movie and session time
movie_title = tk.Label(tickets, text=None, font=(font_name, 20), fg=btn_col, bg=bg_col,
                       wraplength=180, justify="center")
place(movie_title, 0.15, 0.5)

time_label = tk.Label(tickets, text=None, justify="center", font=(font_name, 20),
                      fg=btn_col, bg=bg_col)
place(time_label, 0.15, 0.7)

image = tk.Label(tickets, image=None, bg=bg_col)
place(image, 0.15, 0.3)


# Page widgets

title_label = tk.Label(tickets, text="Tickets", font=(font_name, 30), fg=btn_col, bg=bg_col)
place(title_label, 0.5, 0.075)

fra = tk.Label(tickets, image=widget_bg, bg=bg_col)
place(fra, 0.6, 0.55)

seat_amt = tk.Label(fra, font=(font_name, 25), fg=btn_col, bg=img_bg)
place(seat_amt, 0.5, 0.1)


# Seat type labels
adult = tk.Label(fra, image=type_bg, bg=img_bg)
place(adult, 0.5, 0.2)
adt_info = tk.Label(adult, text="Adult \t ${:.2f}".format(costs["adult"]), fg=fg_col, bg=btn_col,
                    font=(font_name, 20))
place(adt_info, 0.3, 0.5)

child = tk.Label(fra, image=type_bg, bg=img_bg)
place(child, 0.5, 0.4)
chd_info = tk.Label(child, text="Child \t ${:.2f}".format(costs["child"]), fg=fg_col, bg=btn_col,
                    font=(font_name, 20))
place(chd_info, 0.3, 0.5)

student = tk.Label(fra, image=type_bg, bg=img_bg)
place(student, 0.5, 0.6)
stdn_info = tk.Label(student, text="Student \t ${:.2f}".format(costs["student"]), fg=fg_col, bg=btn_col,
                    font=(font_name, 20))
place(stdn_info, 0.3, 0.5)

pensioner = tk.Label(fra, image=type_bg, bg=img_bg)
place(pensioner, 0.5, 0.8)
psr_info = tk.Label(pensioner, text="Pensioner  ${:.2f}".format(costs["pensioner"]), fg=fg_col, bg=btn_col,
                    font=(font_name, 20))
place(psr_info, 0.3, 0.5)


adt = seat_type(adult, adt_tickets, None)
chd = seat_type(child, chd_tickets, None)
stdn = seat_type(student, stdn_tickets, None)
psr = seat_type(pensioner, psr_tickets, None)


# find way to save ticket amounts


# Page controlling buttons
back = create_button(fra, "Back", fg_col, btn_col, 0.15, 0.95, screen_back)
forward = create_button(fra, "Confirm", fg_col, btn_col, 0.85, 0.95, screen_forward)