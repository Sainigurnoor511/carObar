import sv_ttk
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk


class BuyCarPage:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("1000x700")
        self.root.title("CarOBar -- Buy Car")
        self.root.resizable(width=False, height=False)
        self.root.configure(bg='#fff')
        sv_ttk.set_theme("dark")

    def buy_car_page_widgets(self):

        self.frame = tkinter.Frame(self.root, width=1000, height=700)
        self.frame.place(x=0, y=0)

        self.heading = ttk.Label(self.frame, text='buy car', foreground='#c5d0e0', font=('Harlow Solid Italic', 40, 'normal'))
        self.heading.place(x=420, y=5)

        #!_________________________________________________________________________________________________________

        self.brand = ttk.Label(self.frame,text='Select Brand', width=27, foreground='#c5d0e0', font=('Harlow Solid Italic', 16, 'normal'))
        self.brand.place(x=80, y=110)

        self.selectbrand = ttk.Combobox(self.root, width=27, textvariable="Select Brand")
        self.selectbrand['values'] = (  ' Maruti', 
                                        ' Mustang', 
                                        ' Shelby', 
                                        ' Honda', 
                                        ' Renualt', 
                                        ' Hyundai',)

        self.selectbrand.place(x=80, y=140)
        self.selectbrand.current()

        #!_________________________________________________________________________________________________________

        self.budget = ttk.Label(self.frame,text='Select Budget', width=27, foreground='#c5d0e0', font=('Harlow Solid Italic', 16, 'normal'))
        self.budget.place(x=398, y=110)

        self.selectbudget = ttk.Combobox(self.root, width=27, textvariable="Select Brand")
        self.selectbudget['values'] = ( '0 - 3,00,000', 
                                        '3,00,000 - 7,00,000', 
                                        'Above 7,00,000')

        self.selectbudget.place(x=398, y=140)
        self.selectbudget.current()

        #!_________________________________________________________________________________________________________

        self.new_used = ttk.Label(self.frame,text='New / Used', width=27, foreground='#c5d0e0', font=('Harlow Solid Italic', 16, 'normal'))
        self.new_used.place(x=705, y=110)

        self.select_new_used = ttk.Combobox(self.root, width=27, textvariable="Select Brand")
        self.select_new_used['values'] = ('New ','Used')
        self.select_new_used.place(x=705, y=140)
        self.select_new_used.current()


if __name__ == "__main__":
    sell = BuyCarPage()
    sell.buy_car_page_widgets()
    sell.root.mainloop()