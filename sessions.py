import tkinter as tk

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
import datetime
dt = datetime.datetime.now()
first = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n\n1:00pm"
second = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n\n2:00pm"
third = f"{dt.strftime('%d')}/{dt.strftime('%m')}/{dt.strftime('%y')}\n\n3:00pm"

# Placeholder for window location
window = None

session_screen = tk.Frame(window, bg=bg_col)
session_screen.pack(expand=True, fill="both")


class create_button:

    def next_screen(self):
        session_screen.pack_forget()
        import seats as se
        se.seats.pack(expand=True, fill="both")

        # Displays selected movie title on next page
        if self.movie_num == 1:
            se.movie_title.config(text="Spider-Man: Across the Spider-Verse")
            se.movie_title.place(relx=0.525, rely=0.1, anchor="center")
            se.image.config(image=spider)

        elif self.movie_num == 2:
            se.movie_title.config(text="Barbie")
            se.movie_title.place(relx=0.25, rely=0.1, anchor="center")
            se.image.config(image=barbie)

        elif self.movie_num == 3:
            se.movie_title.config(text="The Super Mario Bros. Movie")
            se.movie_title.place(relx=0.45, rely=0.1, anchor="center")
            se.image.config(image=mario)

        if self.text == first:
            se.time_label.config(text=self.text)
        elif self.text == second:
            se.time_label.config(text=self.text)
        else:
            se.time_label.config(text=self.text)

    def __init__(self, location, text, fg, bg, x, y, movie_num):
        self.location = location
        self.text = text
        self.fg = fg
        self.bg = bg
        self.x = x
        self.y = y
        self.movie_num = movie_num
        self.but = tk.Button(self.location, text = self.text, fg = self.fg, background= self.bg,
                             justify="center", font = (font_name, 16), height = 3, border=0, command=self.next_screen)
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
picture = tk.Label(movie_one, image=spider, bg = img_bg)
picture.place(relx=0.1, rely=0.5, anchor="center")

# Movie one title text
title_mo = tk.Label(movie_one, text="Spider-Man: Across the Spider-Verse", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mo.place(relx=0.45, rely=0.15, anchor="center")

# Session buttons
so_mo = create_button(movie_one, first, fg_col, btn_col, 0.3, 0.6, 1)
st_mo = create_button(movie_one, second, fg_col, btn_col, 0.5, 0.6, 1)
sth_mo = create_button(movie_one, third, fg_col, btn_col, 0.7, 0.6, 1)

# --------------------------------------------------------------------

# Second movie section
# Movie two background
movie_two = tk.Label(session_screen, image = bimg, bg = bg_col)
movie_two.place(relx=0.5, rely=0.55, anchor="center")

# Placeholder movie image
picture = tk.Label(movie_two, image=barbie, bg = img_bg)
picture.place(relx=0.1, rely=0.5, anchor="center")

# Movie two title text
title_mt = tk.Label(movie_two, text="Barbie", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mt.place(relx=0.275, rely=0.15, anchor="center")

# Session buttons
so_mt = create_button(movie_two, first, fg_col, btn_col, 0.3, 0.6, 2)
st_mt = create_button(movie_two, second, fg_col, btn_col, 0.5, 0.6, 2)
sth_mt = create_button(movie_two, third, fg_col, btn_col, 0.7, 0.6, 2)

# --------------------------------------------------------------------

# Third movie section
# Movie three background
movie_three = tk.Label(session_screen, image = bimg, bg = bg_col)
movie_three.place(relx=0.5, rely=0.85, anchor="center")

# Placeholder movie image
picture = tk.Label(movie_three, image=mario, bg = img_bg)
picture.place(relx=0.1, rely=0.5, anchor="center")

# Movie three title text
title_mth = tk.Label(movie_three, text="The Super Mario Bros. Movie", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mth.place(relx=0.4, rely=0.15, anchor="center")

# Session buttons
so_mth = create_button(movie_three, first, fg_col, btn_col, 0.3, 0.6, 3)
st_mth = create_button(movie_three, second, fg_col, btn_col, 0.5, 0.6, 3)
sth_mth = create_button(movie_three, third, fg_col, btn_col, 0.7, 0.6, 3)
