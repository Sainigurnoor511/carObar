from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mainpage, database


class BuyCarPage:

    def __init__(self):
        self.root = Tk()
        self.root.title("carObar -- Buy Car")
        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        # self.root.resizable(width =False, height= False)

        # self.root.protocol("WM_DELETE_WINDOW",self.open_home_page)


    def select_car_widgets(self):

        self.frame = Frame(self.root, width=1000, height=250, background="white")
        self.frame.place(x=0, y=0)
        
        self.heading = ttk.Label(self.frame, text='buy car', foreground='#57A1F8', background="white", font=('Harlow Solid Italic', 40, 'normal'))
        self.heading.place(x=416, y=5)




        self.car_brand = ttk.Label(self.frame,text='Select Brand', width=27, foreground='#57A1F8', background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_brand.place(x=80, y=110)

        self.car_brands = []
        for i in database.manage_cars_stock():
            self.car_brands.append(i[2])

        self.selectbrand = ttk.Combobox(self.root, values=self.car_brands, width=27)
        self.selectbrand['state'] = 'readonly'
        self.selectbrand.set("Select Brand")
        self.selectbrand.place(x=80, y=140)




        self.budget = ttk.Label(self.frame,text='Select Budget', width=27, foreground='#57A1F8', background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.budget.place(x=398, y=110)


        self.selectbudget = ttk.Combobox(self.root, width=27)
        self.selectbudget['values'] = ( '0 - 3,00,000', 
                                        '3,00,000 - 7,00,000', 
                                        'Above 7,00,000')
        self.selectbudget['state'] = 'readonly'
        self.selectbudget.set("Select Budget")
        self.selectbudget.place(x=398, y=140)




        self.new_used = ttk.Label(self.frame,text='New / Used', width=27, foreground='#57A1F8', background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.new_used.place(x=705, y=110)

        self.select_new_used = ttk.Combobox(self.root, width=27)
        self.select_new_used['values'] = ('New ','Used')
        self.select_new_used['state'] = 'readonly'
        self.select_new_used.set("Select New/Used")
        self.select_new_used.place(x=705, y=140)



    def show_car_widgets(self):

        self.frame = Frame(self.root,width=1000, height=450, background="white" )
        self.frame.place(x=0, y=231)

        self.y2 = ttk.Label(self.frame,text= 'Available Cars', foreground='#57A1F8', background= "white", font=('Bahnschrift SemiBold Condensed', 30, 'bold'))
        self.y2.place(x=398, y=10)

        self.c1 = ttk.Label(self.frame,text= 'Honda Civic', foreground='#2F60D8', background= "white", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.c1.place(x=368, y=100)
        
        self.c2 = ttk.Label(self.frame,text= 'Maruti Dzire', foreground='#2F60D8', background= "white", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.c2.place(x=368, y=150)

        self.c3 = ttk.Label(self.frame,text= 'Hyundai Aura', foreground='#2F60D8', background= "white", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.c3.place(x=368, y=200)

        self.c4 = ttk.Label(self.frame,text= 'Renault Kiger', foreground='#2F60D8', background= "white", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.c4.place(x=368, y=250)

        self.c4 = ttk.Label(self.frame,text= 'Kia Seltos', foreground='#2F60D8', background= "white", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        self.c4.place(x=368, y=300)

        self.c1 = Button(self.frame, text=' More Car Info', command= self.honda_civic)
        self.c1.place(x=530, y=100)

        self.c1 = ttk.Button(self.frame, text=' View Car Info')
        self.c1.place(x=530, y=150)

        self.c1 = ttk.Button(self.frame, text=' View Car Info')
        self.c1.place(x=530, y=200)

        self.c1 = ttk.Button(self.frame, text=' View Car Info')
        self.c1.place(x=530, y=250)

        self.c1 = ttk.Button(self.frame, text=' View Car Info')
        self.c1.place(x=530, y=300)

        

    def honda_civic(self):
        self.frame = Frame(self.root,width=1000, height=450, background="black" )
        self.frame.place(x=0, y=231)

    def honda_civic(self):
        self.frame = Frame(self.root,width=1000, height=450, background="black" )
        self.frame.place(x=0, y=231)

    def honda_civic(self):
        self.frame = Frame(self.root,width=1000, height=450, background="black" )
        self.frame.place(x=0, y=231)

    def honda_civic(self):
        self.frame = Frame(self.root,width=1000, height=450, background="black" )
        self.frame.place(x=0, y=231)

    def honda_civic(self):
        self.frame = Frame(self.root,width=1000, height=450, background="black" )
        self.frame.place(x=0, y=231)

        
        
        
        d = database.get_cars()
        for i in d:
            print(i[3])

        
        # self.y3 = ttk.Label(self.frame,text= f" {i[2]}  {i[3]}", foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        # self.y3.place(x=80, y=130)

        # self.y4 = ttk.Label(self.frame,text= 'EMI Starting Rs. 833,333/Month', , foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        # self.y4.place(x=80, y=170)

        # self.km_driven = ttk.Label(self.frame,text= ' 0 km', width=10, foreground='#57A1F8', background="#454443", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        # self.km_driven.place(x=40, y=480)

        # self.ownership = ttk.Label(self.frame,text= ' Dealership', width=10, foreground='white', background="#57A1F8", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        # self.ownership.place(x=160, y=480)

        # self.fueltype = ttk.Label(self.frame,text= ' Petrol', width=7, foreground='#57A1F8', font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        # self.fueltype.place(x=280, y=480)

        # self.rto = ttk.Label(self.frame,text= ' PB-07', width=7, foreground='#57A1F8', font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
        # self.rto.place(x=375, y=480)
    

    # def open_home_page(self):
    #     self.root.destroy()
    #     n = mainpage.HomePage()
    #     n.homepage_widgets()    


if __name__ == "__main__":
    buy = BuyCarPage()
    buy.select_car_widgets()
    buy.show_car_widgets()
    buy.root.mainloop()