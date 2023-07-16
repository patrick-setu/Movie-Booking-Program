import tkinter as tk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

widget_bg = tk.PhotoImage(file="ticket_rect.png")
type_bg = tk.PhotoImage(file="type_rect.png")

costs = {"adult": 10, "child": 7.5, "student": 9, "pensioner": 7}

seat_data = open("seat_data.txt", "r")
all_lines = seat_data.readlines()


def screen_back():
    tickets.pack_forget()
    import seats as se
    se.seats.pack(expand=True, fill="both")

class place:

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

tot = 5
adt_tickets = 0
chd_tickets = 0
stdn_tickets = 0
psr_tickets = 0

class seat_type:


    # get total selected from read file


    def __init__(self, location, type):
        self.location = location
        self.type = type
        self.decr = create_button(self.location, "-", fg_col, btn_col, 0.7, 0.5, None)
        self.lab = tk.Label(self.location, text=None, fg=fg_col, bg="white", height=2,
                            width=3)
        place(self.lab, 0.8, 0.5)
        self.incr = create_button(self.location, "+", fg_col, btn_col, 0.9, 0.5)

    def increase(self, total_seats, type):
        if (total_seats > 0):
            print("hello")
            total_seats -= 1
            type += 1
            self.lab.config(text=type)
        else:
            print("no u cant")

        return total_seats, type

    def test(self):
        print("hello")
        self.lab.config(text="hello")


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

seat_amt = tk.Label(fra, text=f"Total seats selected: {all_lines[1]}", font=(font_name, 25), fg=btn_col, bg=img_bg)
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


seat_type(adult, adt_tickets)
# seat_type(child)
# seat_type(student)
# seat_type(pensioner)


# Page controlling buttons
back = create_button(fra, "Back", fg_col, btn_col, 0.15, 0.95, comm=screen_back)
forward = create_button(fra, "Confirm", fg_col, btn_col, 0.85, 0.95, None)

seat_data.close()