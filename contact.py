import tkinter as tk

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

def screen_forward():
    contact.pack_forget()
    import end as e
    e.end.pack(expand=True, fill="both")

class place:
    # Widget placing class shorthand
    def __init__(self, widget, x, y, anchor = "center"):
        self.widget = widget
        self.x = x
        self.y = y
        self.anchor = anchor
        self.widget.place(relx=self.x, rely=self.y, anchor=self.anchor)

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
place(image, 0.15, 0.3)
movie_title = tk.Label(display_bg, font=(font_name, 16), fg=btn_col, bg=img_bg,
                       wraplength=150, justify="center")
place(movie_title, 0.15, 0.7)
time_label = tk.Label(display_bg, justify="center", font=(font_name, 16),
                      fg=btn_col, bg=img_bg)
place(time_label, 0.15, 0.9)

title_label = tk.Label(display_bg, text="Tickets", font=(font_name, 30), fg=fg_col, bg=img_bg)
place(title_label, 0.6, 0.1)

# Displays each ticket total and cost
show_summary = tk.Label(display_bg, text=None, width=30, fg=fg_col, bg=btn_col,
                        font=(font_name, 20))
show_summary.place(relx=0.6, rely=0.5, anchor="center")

# Displays final total
total = tk.Label(display_bg, fg=btn_col, bg=img_bg, font=(font_name, 25, "bold"))
place(total, 0.6, 0.9)

# Contact labels and entryboxes
name_label = tk.Label(contact, text="Full name", fg=btn_col, bg=bg_col,
                      font=(font_name, 16))
place(name_label, 0.275, 0.475, "nw")
name_entry = tk.Entry(contact, textvariable="hello", fg="grey", font=(font_name, 16),
                      width=45)
place(name_entry, 0.5, 0.55)

email_label = tk.Label(contact, text="Email address", fg=btn_col, bg=bg_col,
                      font=(font_name, 16))
place(email_label, 0.275, 0.585, "nw")
email_entry = tk.Entry(contact, fg="grey", font=(font_name, 16), width=45)
place(email_entry, 0.5, 0.66)

# Card information entryboxes disabled
# so no input required

card_label = tk.Label(contact, text="Card number", fg=btn_col, bg=bg_col,
                      font=(font_name, 16))
place(card_label, 0.275, 0.695, "nw")
card_entry = tk.Entry(contact, fg="black", font=(font_name, 16), width=45,
                     state= "disabled")
place(card_entry, 0.5, 0.77)

cvc_label = tk.Label(contact, text="CVC", fg=btn_col, bg=bg_col,
                      font=(font_name, 16))
place(cvc_label, 0.275, 0.805, "nw")
cvc_entry = tk.Entry(contact, fg="black", font=(font_name, 16), width=45,
                     state= "disabled")
place(cvc_entry, 0.5, 0.88)

back = create_button(contact, "Back", fg_col, btn_col, 0.45, 0.95, comm=screen_back)
forward = create_button(contact, "Confirm", fg_col, btn_col, 0.55, 0.95, comm=screen_forward)