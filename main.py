# Importing modules/tinker
import tkinter as tk
from tkinter import font
from email.message import EmailMessage
import ssl
import smtplib

# hello
# Creating and setting tinker settings
window = tk.Tk()
window.title("Movie Booking Program")
window.geometry("996x720")
window.config(bg="#EEF4ED")
# window.resizable(False, False)


# Creating short-hand for widget settings
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
font_name = "Yu Gothic Ui Semilight"


def change_frame1():

    email_sender = "patrickpython644@gmail.com"
    email_password = "zngjckgvhsmewdwp"
    email_receiver = "psetu12@gmail.com"

    subject = "hello"
    body = "text"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)

        smtp.sendmail(email_sender, email_receiver, em.as_string())

    import sessions as ss
    ss.window = window
    st.start_screen.pack_forget()


# Importing file here for no error
import start as st
st.window = window
st.book_btn.config(command = change_frame1)


window.mainloop()