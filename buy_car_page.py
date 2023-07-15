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
        # self.selectbrand.current()

        #!_________________________________________________________________________________________________________

        self.budget = ttk.Label(self.frame,text='Select Budget', width=27, foreground='#c5d0e0', font=('Harlow Solid Italic', 16, 'normal'))
        self.budget.place(x=398, y=110)

        self.selectbudget = ttk.Combobox(self.root, width=27, textvariable="Select Brand")
        self.selectbudget['values'] = ( '0 - 3,00,000', 
                                        '3,00,000 - 7,00,000', 
                                        'Above 7,00,000')

        self.selectbudget.place(x=398, y=140)
        # self.selectbudget.current()

        #!_________________________________________________________________________________________________________

        self.new_used = ttk.Label(self.frame,text='New / Used', width=27, foreground='#c5d0e0', font=('Harlow Solid Italic', 16, 'normal'))
        self.new_used.place(x=705, y=110)

        self.select_new_used = ttk.Combobox(self.root, width=27, textvariable="Select Brand")
        self.select_new_used['values'] = ('New ','Used')
        self.select_new_used.place(x=705, y=140)
        # self.select_new_used.current()

        #!_________________________________________________________________________________________________________


        self.divider = ttk.Label(self.frame,text= '______________________________________________________________________________________________________________', width=89, foreground='#c5d0e0', background="#1C1C1C", font=('Bahnschrift SemiBold Condensed', 20, 'normal'))
        self.divider.place(x=10, y=180)


        #!_______________________________________________________________________________________________________________

        self.image_path = Image.open('images/car.png').resize((350,200))
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.image_label = ttk.Label(self.root, image=self.imgTk)
        self.image_label.place(x=40, y=250)

        self.year = ttk.Label(self.frame,text= ' 2018  Mclaren', width=20, foreground='#c5d0e0', font=('Bahnschrift SemiBold Condensed', 15, 'normal'))
        self.year.place(x=450, y=265)

        self.y2 = ttk.Label(self.frame,text= ' Mclaren x2 | 7 Gear Transmission', width=40, foreground='#c5d0e0', font=('Bahnschrift SemiBold Condensed', 15, 'normal'))
        self.y2.place(x=450, y=300)

        self.y3 = ttk.Label(self.frame,text= ' Rs. 20,000,000 ', width=20, foreground='#c5d0e0', font=('Bahnschrift SemiBold Condensed', 15, 'normal'))
        self.y3.place(x=450, y=335)

        self.y4 = ttk.Label(self.frame,text= 'EMI Starting Rs. 833,333/Month', width=40, foreground='#c5d0e0', font=('Bahnschrift SemiBold Condensed', 15, 'normal'))
        self.y4.place(x=450, y=370)
        
        #!_____________________________________________________________________________________________________________

        self.km_driven = ttk.Label(self.frame,text= ' 0 km', width=10, foreground='#c5d0e0', background="#454443", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.km_driven.place(x=40, y=480)

        self.ownership = ttk.Label(self.frame,text= ' Dealership', width=10, foreground='#c5d0e0', background="#454443", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.ownership.place(x=160, y=480)

        self.fueltype = ttk.Label(self.frame,text= ' Petrol', width=7, foreground='#c5d0e0', background="#454443", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.fueltype.place(x=280, y=480)

        self.rto = ttk.Label(self.frame,text= ' PB-07', width=7, foreground='#c5d0e0', background="#454443", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.rto.place(x=375, y=480)


if __name__ == "__main__":
    buy = BuyCarPage()
    buy.buy_car_page_widgets()
    buy.root.mainloop()