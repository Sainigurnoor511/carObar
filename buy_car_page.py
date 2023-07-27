import sv_ttk
from tkinter import *
import tkinter
from tkinter import ttk
from PIL import Image, ImageTk
import new_mainpage
import database


class BuyCarPage:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Buy Car")
        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.resizable(width =False, height= False)
        # self.root.protocol("WM_DELETE_WINDOW",self.open_home_page)
        sv_ttk.set_theme("light")


    def select_car_widgets(self):

        self.frame = tkinter.Frame(self.root, width=1000, height=250)
        self.frame.place(x=0, y=0)
        
        self.heading = ttk.Label(self.frame, text='buy car', foreground='#57A1F8', font=('Harlow Solid Italic', 40, 'normal'))
        self.heading.place(x=420, y=5)




        self.car_brand = ttk.Label(self.frame,text='Select Brand', width=27, foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.car_brand.place(x=80, y=110)

        self.selectbrand = ttk.Combobox(self.root, width=27)
        self.selectbrand['values'] = (  ' Maruti', 
                                        ' Mustang', 
                                        ' Shelby', 
                                        ' Honda', 
                                        ' Renualt', 
                                        ' Hyundai',)
        self.selectbrand['state'] = 'readonly'
        self.selectbrand.set("Select Brand")
        self.selectbrand.place(x=80, y=140)


        self.budget = ttk.Label(self.frame,text='Select Budget', width=27, foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.budget.place(x=398, y=110)

        self.selectbudget = ttk.Combobox(self.root, width=27)
        self.selectbudget['values'] = ( '0 - 3,00,000', 
                                        '3,00,000 - 7,00,000', 
                                        'Above 7,00,000')
        self.selectbudget['state'] = 'readonly'
        self.selectbudget.set("Select Budget")
        self.selectbudget.place(x=398, y=140)


        self.new_used = ttk.Label(self.frame,text='New / Used', width=27, foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.new_used.place(x=705, y=110)

        self.select_new_used = ttk.Combobox(self.root, width=27)
        self.select_new_used['values'] = ('New ','Used')
        self.select_new_used['state'] = 'readonly'
        self.select_new_used.set("Select New/Used")
        self.select_new_used.place(x=705, y=140)




        #!_________________________________________________________________________________________________________

        self.divider = ttk.Label(self.frame,text= '__________________________________________________________________________________________________________________', width=100, foreground='#c5d0e0', background="white", font=('Bahnschrift SemiBold Condensed', 20, 'normal'))
        self.divider.place(x=0, y=200)

        #!_______________________________________________________________________________________________________________


    def show_car_widgets(self):

        self.frame = tkinter.Frame(self.root, width=1000, height=450)
        self.frame.place(x=0, y=231)

        self.image_path = Image.open('images/Cars/NewCars/honda civic.png').resize((350,200))
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.image_label = ttk.Label(self.frame, image=self.imgTk)
        self.image_label.place(x=80, y=0)


        for i in database.get_cars(2):

            self.car_type = ttk.Label(self.frame, text= i[1], width=20, foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_type.place(x=550, y=50)

            self.car_brand = ttk.Label(self.frame, text= i[2], width=40, foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_brand.place(x=550, y=90)

            self.car_model = ttk.Label(self.frame, text= i[3], width=20, foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_model.place(x=620, y=90)

            self.car_variant = ttk.Label(self.frame, text= i[4], width=40, foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_variant.place(x=550, y=130)

            self.car_mileage = ttk.Label(self.frame, text= i[5], width=10, foreground='#57A1F8', background="#454443", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
            self.car_mileage.place(x=620, y=130)

            # self.ownership = ttk.Label(self.frame, text= i[6], width=10, foreground='white', background="#57A1F8", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
            # self.ownership.place(x=160, y=200)

            # self.fueltype = ttk.Label(self.frame, text= i[7], width=7, foreground='#57A1F8', font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
            # self.fueltype.place(x=280, y=200)

            # self.rto = ttk.Label(self.frame, text= i[8], width=7, foreground='#57A1F8', font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
            # self.rto.place(x=375, y=200)
        
            print()
            print("ID =", i[0])
            print("car type =", i[1])
            print("car brand =", i[2])
            print("car model =", i[3])
            print("car variant =", i[4])
            print("car mileage =", i[5])

            # self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5], "Delete", "Update"))






        # self.year = ttk.Label(self.frame,text= self.car_brand, width=20, foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 15, 'normal'))
        # self.year.place(x=550, y=50)

        # self.y2 = ttk.Label(self.frame,text= ' Mclaren x2 | 7 Gear Transmission', width=40, foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 15, 'normal'))
        # self.y2.place(x=550, y=90)

        # self.y3 = ttk.Label(self.frame,text= ' Rs. 20,000,000 ', width=20, foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 15, 'normal'))
        # self.y3.place(x=550, y=130)

        # self.y4 = ttk.Label(self.frame,text= 'EMI Starting Rs. 833,333/Month', width=40, foreground='#2F60D8', font=('Bahnschrift SemiBold Condensed', 15, 'normal'))
        # self.y4.place(x=550, y=170)
        
        # #!_____________________________________________________________________________________________________________

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
    #     n = new_mainpage.HomePage()
    #     n.homepage_widgets()    


if __name__ == "__main__":
    buy = BuyCarPage()
    buy.select_car_widgets()
    buy.show_car_widgets()
    buy.root.mainloop()