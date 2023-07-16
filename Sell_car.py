from tkinter import *
from tkinter import ttk
import Sell_car_database
from tkinter import messagebox


class Sellcar:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x730")
        self.root.title("Sell Car") 
        self.root.configure(bg ='white')
        self.root.resizable(width =False, height= False)



    def sellcar_widgets(self):

    ###---------------------------------/////// SELL CAR DETAILS //////------------------------------##

        self.sellcar_frame = Frame(self.root, width=1000,height=730,bg = "#191970")
        self.sellcar_frame.place(x=0,y=0)

        self.title_label = Label(self.sellcar_frame, text="------ Enter Car Details ------",bg = "#191970",fg='white',font=('Microsoft YaHei UI Light',14,'bold'))
        self.title_label.place(x=390,y=15)

        
        self.car_brand = Label(self.sellcar_frame,text="Enter the Car Brand",font = 20,fg='white',bg = '#191970')
        self.car_brand.place(x=30,y=90,width=180, height=30)
        self.car_brand_entry = Entry(self.sellcar_frame, font =20 )
        self.car_brand_entry.place(x =220,y =90,width =180,height=30)
  
        self.car_model = Label(self.sellcar_frame,text="Enter the Car Model",font = 20,fg='white',bg = '#191970')
        self.car_model.place(x=30,y=180,width=180, height=30)
        self.car_model_entry= Entry(self.sellcar_frame, font =20 )
        self.car_model_entry.place(x =220,y =180,width =180,height=30)

        # -------------/////////  COMBOBOXES //////////----------------#

        self.car_reg = Label(self.sellcar_frame,text="Select the Registration Year",font = 20,fg='white',bg = '#191970')
        self.car_reg.place(x=500,y=90,width =200,height=30)
        year =[2023,2022,2021,2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001,2000,1999,1998,1997,1996,1995,1994,1993,1992,1991,1990]
        self.car_reg_cb = ttk.Combobox(self.sellcar_frame, values=year)
        self.car_reg_cb.place(x =750,y =90,width =180,height=30)
        self.car_reg_cb["state"]='readonly'
        self.car_reg_cb.set("Select Year")

        self.car_var = Label(self.sellcar_frame,text="Select Car Variant",font = 20,fg='white',bg = '#191970')
        self.car_var.place(x=480,y=180,width =180,height=30)
        variant =["Petrol","Diesel","Electric","Hybrid"]
        self.car_var_cb = ttk.Combobox(self.sellcar_frame, values=variant)
        self.car_var_cb.place(x =750,y =180,width =180,height=30)
        self.car_var_cb["state"]='readonly'
        self.car_var_cb.set("Select Variant")

        self.car_ownership = Label(self.sellcar_frame,text="Select Car Ownership",font = 20,fg='white',bg = '#191970')
        self.car_ownership.place(x=33,y=280,width =180,height=30)
        ownership =["1st owner","2nd owner","3rd owner","4th owner","5th owner"]
        self.car_ownership_cb = ttk.Combobox(self.sellcar_frame, values=ownership)
        self.car_ownership_cb.place(x =223,y =280,width =180,height=30)
        self.car_ownership_cb["state"]='readonly'
        self.car_ownership_cb.set("Select Ownership")

        self.km_driven = Label(self.sellcar_frame,text="Select km Driven",font = 20,fg='white',bg = '#191970')
        self.km_driven.place(x=480,y=280,width =180,height=30)
        odometer =["0 km - 10,000 km","10,000 km - 20,000 km","20,000 km - 30,000 km","30,000 km - 40,000 km","40,000 km - 50,000 km","50,000 km - 60,000 km","60,000 km - 70,000 km","70,000 km - 80,000 km","80,000 km - 90,000 km","90,000 km - 1,00,000 km","1,00,000 km - 1,10,000 km"]
        self.km_driven_cb = ttk.Combobox(self.sellcar_frame, values=odometer)
        self.km_driven_cb.place(x =750,y =280,width =180,height=30)
        self.km_driven_cb["state"]='readonly'
        self.km_driven_cb.set("odometer")

      #####---------------------------///// SELLER DETAILS  //////--------------------------------------------#####

        self.title2_label = Label(self.sellcar_frame, text="------ Seller Details ------",bg = "#191970",fg='white',font=('Microsoft YaHei UI Light',14,'bold'))
        self.title2_label.place(x=400,y=400)

        self.seller_name = Label(self.sellcar_frame,text="Seller Name",font = 20,fg='white',bg = '#191970')
        self.seller_name.place(x=10,y=480,width=180, height=30)
        self.seller_name_entry = Entry(self.sellcar_frame, font =20 )
        self.seller_name_entry.place(x =220,y =480,width =180,height=30) 

        self.seller_address = Label(self.sellcar_frame,text="Seller Address",font = 20,fg='white',bg = '#191970')
        self.seller_address.place(x=10,y=560,width=180, height=30)
        self.seller_address_entry = Entry(self.sellcar_frame, font =20 )
        self.seller_address_entry.place(x =220,y =560,width =180,height=30) 

        self.seller_mobile = Label(self.sellcar_frame,text="Seller Contact No.",font = 20,fg='white',bg = '#191970')
        self.seller_mobile.place(x=480,y=480,width=180, height=30)
        self.seller_mobile_entry = Entry(self.sellcar_frame, font =20 )
        self.seller_mobile_entry.place(x =750,y =480,width =180,height=30)


        self.sign_up = Button(self.sellcar_frame,width=12,text='Register', border=0,bg='#FF8247',font=10,command=self.get_sell_car_data)
        self.sign_up.place(x=450,y=660)

        self.root.mainloop()

        #------------------------------//////// GETTING CAR DATA ///////----------------------------###

    def get_sell_car_data(self):

        if self.car_brand_entry.get() == "":
            messagebox.showwarning("Alert!","Please enter the car brand")

        elif self.car_reg_cb.get() =="":
            messagebox.showwarning("Alert!","Please select registration year")
            
        elif self.car_model_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter the car model")
            
        elif self.car_var_cb.get() =="":
            messagebox.showwarning("Alert!","Please select variant")
            
        elif self.car_ownership_cb.get() =="":
            messagebox.showwarning("Alert!","Please select car ownership")

        elif self.km_driven_cb.get() =="":
            messagebox.showwarning("Alert!","Please select km driven")

        elif self.seller_name_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter seller name")

        elif self.seller_mobile_entry.get()=="":
            messagebox.showwarning("Alert!","Please enetr seller's contact number")

        elif self.seller_address_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter seller's address")

        else:
            carBrand =  self.car_brand_entry.get()
            registrationYear = self.car_reg_cb.get()
            carModel =  self.car_model_entry.get()
            carVariant = self.car_var_cb.get()
            carOwnership = self.car_ownership_cb.get()
            kmDriven= self.km_driven_cb.get()


            sellerName = self.seller_name_entry.get()
            sellerContact=self.seller_mobile_entry.get()
            sellerAddress = self.seller_address_entry.get()

            a = (carBrand,registrationYear,carModel, carVariant,carOwnership,kmDriven,sellerName, sellerContact,sellerAddress)
            print(a)

            ###----------------------//////// CONNECTING WITH DATABASE ///////-----------------------------#

            result = Sell_car_database.add_car_and_seller_details(a)
            if result:
                    messagebox.showinfo("Message","Car & Seller details added successfully")
                    self.root.destroy()
                
            else:
                    messagebox.showerror("Alert!", "Something Went wrong")

        
        







       

s = Sellcar()
s.sellcar_widgets()
