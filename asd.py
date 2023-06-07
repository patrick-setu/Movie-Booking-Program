import tkinter as tk

window = tk.Tk()
window.title("Movie Booking Program")
window.geometry("600x500")

#get window  size and create fixed window size

window.config(background="red")
print(window.winfo_screenheight())
window.mainloop()