import tkinter
from tkinter import ttk
import sv_ttk

class Dashboard:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("1000x700")
        self.root.title("CarOBar")
        self.root.resizable(width =False, height= False)
        self.root.configure(bg ='#fff')
        sv_ttk.set_theme("light")

    def widgetss(self):
        self.button = ttk.Button(self.root, text="Click me!")
        self.button.place(x=100, y=100)

        self.combobox = ttk.Combobox(self.root, text="brand")
        self.combobox.place(x=100, y=200)

d = Dashboard()
d.widgetss()
d.root.mainloop()