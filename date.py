from tkinter import *
from tkcalendar import DateEntry
t = Tk()

t.title("Date Widget")

d = DateEntry(t)
d.pack()

t.mainloop()