"""Import tkinter for GUI."""
import tkinter as tk
from tkinter import messagebox
from email.message import EmailMessage
import ssl
import smtplib

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
contact = tk.Frame(window, bg=bg_col)


def check_num(string):
    """Check if there is a number in string."""
    return any(char.isdigit() for char in string)


def screen_back():
    """Return to previous page."""
    contact.pack_forget()
    import tickets as ts

    ts.tickets.pack(expand=True, fill="both")


def screen_forward():
    """Continue if valid data is inputted."""
    if (
        check_num(name_entry.get()) is False
        and len(name_entry.get()) > 0
        and "E.g." not in name_entry.get()
    ):
        if (
            "@" in email_entry.get()
            and len(email_entry.get()) > 0
            and len(email_entry.get()) <= 320
            and "E.g." not in email_entry.get()
        ):

            txt = open("seat_data.txt", "r")
            all_data = txt.readlines()
            email_body = ""
            for each_data in all_data:
                email_body += each_data
            email_body += f"Thank you for booking, {name_entry.get()}"
            txt.close()

            # Sends an email to the user inputted email address
            email_sender = "patrickpython644@gmail.com"
            email_password = "zngjckgvhsmewdwp"
            email_receiver = email_entry.get()

            # Email structure
            subject = f"{movie_title['text']} Receipt"
            body = f"{email_body}"

            # Creates setup of email
            em = EmailMessage()
            em["From"] = email_sender
            em["To"] = email_receiver
            em["Subject"] = subject
            em.set_content(body)

            # Provides secure connection using ssl
            context = ssl.create_default_context()

            # Uses gmail as local host to send the email
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                smtp.login(email_sender, email_password)

                smtp.sendmail(email_sender, email_receiver, em.as_string())

            contact.pack_forget()
            import end as e

            e.end.pack(expand=True, fill="both")
            e.text.config(
                text="Booking has been confirmed!\n\n"
                "Thank you for your purchase.\n\n"
                f"Check your email at {email_entry.get()} to view your tickets"
            )
        else:
            email_entry.delete(0, tk.END)
            messagebox.showerror("Error", "Email not valid")
    else:
        name_entry.delete(0, tk.END)
        messagebox.showerror(
            "Error", "Name section must not contain numbers or be left blank"
        )


class Place:
    """Widget placing class shorthand."""

    def __init__(self, widget, x, y, anchor="center"):
        """Place widget based on x, y."""
        self.widget = widget
        self.x = x
        self.y = y
        self.anchor = anchor
        self.widget.place(relx=self.x, rely=self.y, anchor=self.anchor)


class CreateButton:
    """Create instance of a button."""

    def __init__(self, location, text, fg, bg, x, y, comm=None):
        """Stylise button."""
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


def clear_name(e):
    """Clear name entry when clicked."""
    sentence_length = len("E.g. Patrick Setu")

    if name_entry.get() == "E.g. Patrick Setu":
        for letters in range(sentence_length):
            name_entry.delete(first=0, last=None)
    else:
        pass

    name_entry.unbind("<Button-1")
    name_entry.config(fg="black")


def clear_email(e):
    """Clear email entry when clicked."""
    sentence_length = len("E.g. patricksetu@email.com")

    if email_entry.get() == "E.g. patricksetu@email.com":
        for letters in range(sentence_length):
            email_entry.delete(first=0, last=None)
    else:
        pass

    email_entry.unbind("<Button-1")
    email_entry.config(fg="black")


# Page widgets

display_bg = tk.Label(contact, image=ticket_bg, bg=bg_col, borderwidth=0)
Place(display_bg, 0.5, 0.25)


# Specified movie and session time
image = tk.Label(display_bg)
Place(image, 0.15, 0.3)

movie_title = tk.Label(
    display_bg,
    font=(font_name, 16),
    fg=btn_col,
    bg=img_bg,
    wraplength=150,
    justify="center",
)
Place(movie_title, 0.15, 0.7)

time_label = tk.Label(
    display_bg, justify="center", font=(font_name, 16), fg=btn_col, bg=img_bg
)
Place(time_label, 0.15, 0.9)

title_label = tk.Label(
    display_bg, text="Tickets", font=(font_name, 30), fg=fg_col, bg=img_bg
)
Place(title_label, 0.6, 0.1)

# Displays each ticket total and cost
show_summary = tk.Label(
    display_bg, width=30, fg=fg_col, bg=btn_col, font=(font_name, 18)
)
show_summary.place(relx=0.6, rely=0.5, anchor="center")

# Displays final total
total = tk.Label(display_bg, fg=btn_col, bg=img_bg, font=(font_name, 20, "bold"))
Place(total, 0.6, 0.95)

# Contact labels and entryboxes
name_label = tk.Label(
    contact, text="Full name", fg=btn_col, bg=bg_col, font=(font_name, 16)
)
Place(name_label, 0.275, 0.475, "nw")
name_entry = tk.Entry(contact, fg="grey", font=(font_name, 16), width=45)
Place(name_entry, 0.5, 0.55)
name_entry.insert(0, "E.g. Patrick Setu")
name_entry.bind("<Button-1>", clear_name)

email_label = tk.Label(
    contact, text="Email address", fg=btn_col, bg=bg_col, font=(font_name, 16)
)
Place(email_label, 0.275, 0.585, "nw")
email_entry = tk.Entry(contact, fg="grey", font=(font_name, 16), width=45)
Place(email_entry, 0.5, 0.66)
email_entry.insert(0, "E.g. patricksetu@email.com")
email_entry.bind("<Button-1>", clear_email)

# Card information entryboxes disabled
# so no input required

card_label = tk.Label(
    contact, text="Card number", fg=btn_col, bg=bg_col, font=(font_name, 16)
)
Place(card_label, 0.275, 0.695, "nw")
card_num = tk.StringVar(value="XXXX-XXXX-XXXX-XXXX")
card_entry = tk.Entry(
    contact,
    disabledforeground="black",
    font=(font_name, 16),
    width=45,
    state="disabled",
    textvariable=card_num,
)
Place(card_entry, 0.5, 0.77)

cvc_label = tk.Label(contact, text="CVC", fg=btn_col, bg=bg_col, font=(font_name, 16))
Place(cvc_label, 0.275, 0.805, "nw")
cvc_num = tk.StringVar(value="XXX")
cvc_entry = tk.Entry(
    contact,
    disabledforeground="black",
    font=(font_name, 16),
    width=45,
    state="disabled",
    textvariable=cvc_num,
)
Place(cvc_entry, 0.5, 0.88)

back = CreateButton(contact, "Back", fg_col, btn_col, 0.4, 0.96, comm=screen_back)
forward = CreateButton(
    contact, "Confirm", fg_col, btn_col, 0.6, 0.96, comm=screen_forward
)
