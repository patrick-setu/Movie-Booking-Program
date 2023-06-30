import tkinter as tk

# Constant colour shorthands
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

# Importing images
bimg = tk.PhotoImage(file="rect.png")
mimg = tk.PhotoImage(file="img.png")

# Creating datetime variables
import datetime
dt = datetime.datetime.now()
day = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n\n"

def inserted_time(increase_by):
    time = int(dt.strftime('%I'))
    time += increase_by
    if time > 12:
        time -= 12
    str(time)
    return time

time_one = day,inserted_time(0)
print(time_one)
time_two = day + inserted_time(2)
time_three = day + inserted_time(4)

# Placeholder for window location
window = None

session_screen = tk.Frame(window, bg=bg_col)
session_screen.pack(expand=True, fill="both")


class create_button:

    def next_screen(self):
        session_screen.pack_forget()
        import seats as se

    def __init__(self, location, text, fg, bg, x, y):
        self.location = location
        self.text = text
        self.fg = fg
        self.bg = bg
        self.x = x
        self.y = y
        self.but = tk.Button(self.location, text = self.text, fg = self.fg, bg = self.bg,
                             justify="center", font = (font_name, 16), height = 3, border=0, command=self.next_screen,
                             highlightcolor=bg_col)
        self.but.place(relx = self.x, rely = self.y, anchor = "center")



# Session screen widgets
# Screen title
screen_label = tk.Label(session_screen, text="Currently airing", font=(font_name, 30, "bold"), fg=btn_col, bg=bg_col)
screen_label.place(x=50, y=24)

# --------------------------------------------------------------------

# First movie section
# Movie one background
movie_one = tk.Label(session_screen, image = bimg, bg = bg_col)
movie_one.place(relx=0.5, rely=0.25, anchor="center")

# Placeholder movie image
but = tk.Label(movie_one, image=mimg, bg = img_bg)
but.place(relx=0.1, rely=0.5, anchor="center")

# Movie one title text
title_mo = tk.Label(movie_one, text="Movie Title", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mo.place(relx=0.3, rely=0.15, anchor="center")

# Session buttons
# so_mo = create_button(movie_one, time_one, fg_col, btn_col, 0.3, 0.6)
# st_mo = create_button(movie_one, day_2, fg_col, btn_col, 0.5, 0.6)
# sth_mo = create_button(movie_one, day_3, fg_col, btn_col, 0.7, 0.6)

# --------------------------------------------------------------------

# Second movie section
# Movie two background
movie_two = tk.Label(session_screen, image = bimg, bg = bg_col)
movie_two.place(relx=0.5, rely=0.55, anchor="center")

# Placeholder movie image
but = tk.Label(movie_two, image=mimg, bg = img_bg)
but.place(relx=0.1, rely=0.5, anchor="center")

# Movie two title text
title_mt = tk.Label(movie_two, text="Movie Title", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mt.place(relx=0.3, rely=0.15, anchor="center")

# Session buttons
# so_mt = create_button(movie_two, day_1, fg_col, btn_col, 0.3, 0.6)
# st_mt = create_button(movie_two, day_2, fg_col, btn_col, 0.5, 0.6)
# sth_mt = create_button(movie_two, day_3, fg_col, btn_col, 0.7, 0.6)

# --------------------------------------------------------------------

# Third movie section
# Movie three background
movie_three = tk.Label(session_screen, image = bimg, bg = bg_col)
movie_three.place(relx=0.5, rely=0.85, anchor="center")

# Placeholder movie image
but = tk.Label(movie_three, image=mimg, bg = img_bg)
but.place(relx=0.1, rely=0.5, anchor="center")

# Movie three title text
title_mth = tk.Label(movie_three, text="Movie Title", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mth.place(relx=0.3, rely=0.15, anchor="center")

# Session buttons
# so_mth = create_button(movie_three, day_1, fg_col, btn_col, 0.3, 0.6)
# st_mth = create_button(movie_three, day_2, fg_col, btn_col, 0.5, 0.6)
# sth_mth = create_button(movie_three, day_3, fg_col, btn_col, 0.7, 0.6)

# --------------------------------------------------------------------

# use to get widget height
# print(widget.winfo_reqheight())