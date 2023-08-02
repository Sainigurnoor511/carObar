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
        self.heading.place(x=420, y=5)




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




        #!_________________________________________________________________________________________________________

        self.divider = ttk.Label(self.frame,text= '__________________________________________________________________________________________________________________', width=100, foreground='#c5d0e0', background="white", font=('Bahnschrift SemiBold Condensed', 20, 'normal'))
        self.divider.place(x=0, y=200)

        #!_______________________________________________________________________________________________________________


    def show_car_widgets(self):

        self.frame = Frame(self.root,width=1000, height=1000, background="grey" )
        self.frame.place(x=0, y=231)


        self.vertical_scrollbar = ttk.Scrollbar(self.frame, orient=VERTICAL)
        self.vertical_scrollbar.place(x=982, y=2, height=470)

        # self.frame.configure(yscrollcommand=vertical_scrollbar.set)
        # vertical_scrollbar.place(x=900, y=231, height=4450)

        # horizontal_scrollbar = ttk.Scrollbar(self.f, orient=HORIZONTAL, command=self.tree_view.xview)
        # self.tree_view.configure(xscrollcommand=horizontal_scrollbar.set)
        # horizontal_scrollbar.place(x=16, y=501, width=1115)


        # self.scrollbar = ttk.Scrollbar(self.root)
        # self.scrollbar.place(x=981, y=232, height=465)

        # # Create a Canvas widget with the scrollbar attached
        # self.canvas = Canvas(self.root, yscrollcommand=self.scrollbar.set, background="Gray", width=981, height=470)
        # self.canvas.place(x=-1, y=231)
        # self.scrollbar.config(command=self.canvas.yview)

        d = database.get_cars()
        print(d,type(d),len(d))

        for i in range(0, len(d)):
            print(d[i][1])
            
            print(type(i))
            self.image_path = Image.open('images/Cars/Used Cars/Honda Civic.png').resize((350,200))
            self.imgTk = ImageTk.PhotoImage(self.image_path)
            self.image_label = ttk.Label(self.frame, image=self.imgTk, background="white")
            self.image_label.place(x=100, y=50)

            self.car_type = ttk.Label(self.frame, text= d[i][1], width=40, foreground='#2F60D8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_type.place(x=500, y=50)

            # self.car_brand = ttk.Label(self.canvas, text= d[i][2], width=40, foreground='#2F60D8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            # self.car_brand.place(x=500, y=90)

            # self.car_model = ttk.Label(self.canvas, text= d[i][3], width=30, foreground='#2F60D8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            # self.car_model.place(x=560, y=90)

            # self.car_variant = ttk.Label(self.canvas, text= d[i][4], width=40, foreground='#2F60D8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            # self.car_variant.place(x=500, y=130)

            # self.car_mileage = ttk.Label(self.canvas, text= d[i][5], width=45, foreground='#57A1F8', background="#454443", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
            # self.car_mileage.place(x=500, y=170)

            # self.ownership = ttk.Label(self.frame, text= d[i][6], width=10, foreground='white', background="#57A1F8", font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
            # self.ownership.place(x=160, y=200)

            # self.fueltype = ttk.Label(self.frame, text= d[i][7], width=7, foreground='#57A1F8', font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
            # self.fueltype.place(x=280, y=200)

            # self.rto = ttk.Label(self.frame, text= d[i][8], width=7, foreground='#57A1F8', font=('Bahnschrift SemiBold Condensed', 16, 'normal'))
            # self.rto.place(x=375, y=200)
        
            print()
            print("ID =", d[i][0])
            print("car type =", d[i][1])
            print("car brand =", d[i][2])
            print("car model =", d[i][3])
            print("car variant =", d[i][4])
            print("car mileage =", d[i][5])

        #     self.canvas.create_window((0, 431), anchor=SW)
            
        #     # self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5], "Delete", "Update"))






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
    #     n = mainpage.HomePage()
    #     n.homepage_widgets()    


if __name__ == "__main__":
    buy = BuyCarPage()
    buy.select_car_widgets()
    buy.show_car_widgets()
    buy.root.mainloop()