import tkinter as tk

# Constant
bg_col = "#134074"
fg_col = "#0b2545"
btn_col = "#eef4ed"
img_bg = "#8DA9C4"
font_name = "Yu Gothic Ui Semilight"

# Importing images
bimg = tk.PhotoImage(file="rect.png")
mimg = tk.PhotoImage(file="img.png")

# Placeholder for window location
window = None

session_screen = tk.Frame(window, bg=bg_col)
session_screen.pack(expand=True, fill="both")


class create_button:

    def tester(self):
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
                             justify="center", font = (font_name, 16), height = 3, border=0, command=self.tester,
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

# Movie title text
title_mo = tk.Label(movie_one, text="Movie Title", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mo.place(relx=0.3, rely=0.15, anchor="center")

# Session buttons
so_mo = create_button(movie_one, "25/01/24\n\n01:00pm", fg_col, btn_col, 0.3, 0.6)
st_mo = create_button(movie_one, "26/01/24\n\n02:00pm", fg_col, btn_col, 0.5, 0.6)
sth_mo = create_button(movie_one, "27/01/24\n\n03:00pm", fg_col, btn_col, 0.7, 0.6)

# --------------------------------------------------------------------

# Second movie section
# Movie two background
movie_two = tk.Label(session_screen, image = bimg, bg = bg_col)
movie_two.place(relx=0.5, rely=0.55, anchor="center")

# Placeholder movie image
but = tk.Label(movie_two, image=mimg, bg = img_bg)
but.place(relx=0.1, rely=0.5, anchor="center")

# Movie title text
title_mt = tk.Label(movie_two, text="Movie Title", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mt.place(relx=0.3, rely=0.15, anchor="center")

# Session buttons
so_mt = create_button(movie_two, "25/01/24\n\n01:00pm", fg_col, btn_col, 0.3, 0.6)
st_mt = create_button(movie_two, "26/01/24\n\n02:00pm", fg_col, btn_col, 0.5, 0.6)
sth_mt = create_button(movie_two, "27/01/24\n\n03:00pm", fg_col, btn_col, 0.7, 0.6)

# --------------------------------------------------------------------

# Third movie section
# Movie three background
movie_three = tk.Label(session_screen, image = bimg, bg = bg_col)
movie_three.place(relx=0.5, rely=0.85, anchor="center")

# Placeholder movie image
but = tk.Label(movie_three, image=mimg, bg = img_bg)
but.place(relx=0.1, rely=0.5, anchor="center")

# Movie title text
title_mth = tk.Label(movie_three, text="Movie Title", font=(font_name, 25), fg=fg_col, bg=img_bg)
title_mth.place(relx=0.3, rely=0.15, anchor="center")

# Session buttons
so_mth = create_button(movie_three, "25/01/24\n\n01:00pm", fg_col, btn_col, 0.3, 0.6)
st_mth = create_button(movie_three, "26/01/24\n\n02:00pm", fg_col, btn_col, 0.5, 0.6)
sth_mth = create_button(movie_three, "27/01/24\n\n03:00pm", fg_col, btn_col, 0.7, 0.6)

# --------------------------------------------------------------------

# use to get widget height
# print(widget.winfo_reqheight())