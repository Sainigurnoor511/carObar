from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# import sv_ttk
# sv_ttk.set_theme("light")


class BuyCarPage:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x700")
        self.root.title("CarOBar -- Buy Car")
        self.root.resizable(width =False, height= False)
        self.root.configure(bg ='#fff')

    def buy_car_page_widgets(self):

        self.frame = Frame(self.root,width=1000,height=700,bg='#c5d0e0')
        self.frame.place(x=0,y=0)

        self.heading = Label(self.frame,text ='buy car' , fg='black',bg = '#c5d0e0',font=('Harlow Solid Italic',40,'normal'))
        self.heading.place(x=420,y=5)

        self.monthchoosen = ttk.Combobox(self.root, width = 27, textvariable= "Select Brand")
  
        # Adding combobox drop down list
        self.monthchoosen['values'] = (' January', 
                                ' February',
                                ' March',
                                ' April',
                                ' May',
                                ' June',
                                ' July',
                                ' August',
                                ' September',
                                ' October',
                                ' November',
                                ' December')
  
        self.monthchoosen.grid(column = 1, row = 5)
        self.monthchoosen.current()

if __name__ == "__main__":
    sell = BuyCarPage()
    sell.buy_car_page_widgets()
    sell.root.mainloop()