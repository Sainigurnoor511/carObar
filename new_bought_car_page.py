from tkinter import *
from tkinter import ttk
# import database
# import new_mainpage
from tkinter import messagebox
from PIL import Image, ImageTk
# import sv_ttk

class BoughtCarPage:
    def __init__(self, selected_car=""):
        self.root = Tk()
        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        # sv_ttk.set_theme("light")

        # self.root.protocol("WM_DELETE_WINDOW",self.open_home_page)

        # Here we are getting the data from the parameter regarding
        # the selected car from the display car file
        self.selectedCar = selected_car

        if self.selectedCar:
            self.root.title("Update Used Car")
        else:
            self.root.title("Sell Car")
        

    def new_bought_car_page_widgets(self):

    ###---------------------------------/////// SELL CAR DETAILS //////------------------------------###

        self.brand_new_frame = Frame(self.root, width=1000,height=1000, bg= "white")
        self.brand_new_frame.place(x=0,y=0)

        self.heading = ttk.Label(self.brand_new_frame, text='Brand New Cars', foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 35, 'normal'))
        self.heading.place(x=380, y=0)

        self.title1 = ttk.Label(self.brand_new_frame, text=' Enter Car Details ', foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 19, 'normal'))
        self.title1.place(x=420, y=110)

        self.car_brand = ttk.Label(self.brand_new_frame,text="Car Brand", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_brand.place(x=90, y=190,width=180, height=30)

        self.car_brand_entry = ttk.Entry(self.brand_new_frame, font =20 )
        self.car_brand_entry.place(x =220,y =190,width =180,height=30)


        self.car_model = ttk.Label(self.brand_new_frame,text="Car Model", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_model.place(x=90,y=260,width=250, height=30)

        self.car_model_entry= ttk.Entry(self.brand_new_frame, font =20)
        self.car_model_entry.place(x =220,y =260,width =180,height=30)

        self.car_mileage = ttk.Label(self.brand_new_frame,text="Car Mileage",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_mileage.place(x=570,y=260,width=180, height=30)

        self.car_mileage_entry = ttk.Entry(self.brand_new_frame, font =20 )
        self.car_mileage_entry.place(x =720,y =260,width =180,height=30) 


        self.car_price = ttk.Label(self.brand_new_frame,text="Car Price",foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_price.place(x=90,y=330,width=180, height=30)

        self.car_price_entry = ttk.Entry(self.brand_new_frame, font =20 )
        self.car_price_entry.place(x =220,y =330,width =180,height=30) 


        # -------------/////////  COMBOBOX //////////----------------#

        self.car_var = ttk.Label(self.brand_new_frame,text="Car Variant", foreground='#57A1F8',background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_var.place(x=570, y=190, width=180, height=30)

        variant =["Petrol","Diesel","Electric","Hybrid"]
        self.car_var_cb = ttk.Combobox(self.brand_new_frame, values=variant)
        self.car_var_cb.place(x=720, y=190, width=180, height=30)
        self.car_var_cb["state"]='readonly'
        self.car_var_cb.set("Select Variant")



        self.user_image_path = Image.open('images\mainpage\submit_sellcar_button.png').resize((120,30))
        self.user_imageTk2 = ImageTk.PhotoImage(self.user_image_path)
        print(self.user_image_path)
        self.sign_up = Button(self.brand_new_frame, image= self.user_imageTk2,borderwidth=0,background="white", command=self.get_new_car_data)
        self.sign_up.place(x=440,y=640)

        self.root.mainloop()
        
        #------------------------------//////// GETTING CAR DATA ///////----------------------------###

    def get_new_car_data(self):

        if self.car_brand_entry.get() == "":
            messagebox.showwarning("Alert!","Please enter the car brand")
            
        elif self.car_model_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter the car model")
            
        elif self.car_var_cb.get() =="Select Variant":
            messagebox.showwarning("Alert!","Please select variant")
       
        elif self.car_mileage_entry.get() =="":
            messagebox.showwarning("Alert!","Please enter car mileage")

        elif self.car_price_entry.get()=="":
            messagebox.showwarning("Alert!","Please enter car price")

        else:
            carBrand =  self.car_brand_entry.get()
            carModel =  self.car_model_entry.get()
            carVariant = self.car_var_cb.get()
            carMileage=self.car_mileage_entry.get()
            carPrice = self.car_price_entry.get()
            
            a = (carBrand,carModel, carVariant,carMileage,carPrice)
            print(a)

            ###----------------------//////// CONNECTING WITH DATABASE ///////-----------------------------#

            # result = database.add_car_and_seller_details(a)
            # if result:
            #         messagebox.showinfo("Message","Car & Seller details added successfully")
            #         # self.root.destroy()
                
            # else:
            #         messagebox.showerror("Alert!", "Something Went wrong")





    
    # def get_updated_new_car_data(self):

    #     if self.car_brand_entry.get() == "":
    #         messagebox.showwarning("Alert!","Please enter the car brand")

    #     elif self.car_reg_cb.get() =="Select Year":
    #         messagebox.showwarning("Alert!","Please select registration year")
            
    #     elif self.car_model_entry.get() =="":
    #         messagebox.showwarning("Alert!","Please enter the car model")
            
    #     elif self.car_var_cb.get() =="Select Variant":
    #         messagebox.showwarning("Alert!","Please select variant")
            
    #     elif self.car_ownership_cb.get() =="Select Ownership":
    #         messagebox.showwarning("Alert!","Please select car ownership")

    #     elif self.km_driven_cb.get() =="odometer":
    #         messagebox.showwarning("Alert!","Please select km driven")

    #     elif self.seller_name_entry.get() =="":
    #         messagebox.showwarning("Alert!","Please enter seller name")

    #     elif self.seller_mobile_entry.get()=="":
    #         messagebox.showwarning("Alert!","Please enetr seller's contact number")

    #     elif self.seller_address_entry.get() =="":
    #         messagebox.showwarning("Alert!","Please enter seller's address")

    #     else:
    #         carBrand =  self.car_brand_entry.get()
    #         registrationYear = self.car_reg_cb.get()
    #         carModel =  self.car_model_entry.get()
    #         carVariant = self.car_var_cb.get()
    #         carOwnership = self.car_ownership_cb.get()
    #         kmDriven= self.km_driven_cb.get()


    #         sellerName = self.seller_name_entry.get()
    #         sellerContact=self.seller_mobile_entry.get()
    #         sellerAddress = self.seller_address_entry.get()

    #         u = (carBrand,registrationYear,carModel, carVariant,carOwnership,kmDriven,sellerName, sellerContact,sellerAddress)
    #         dict(self.car_is)
    #         print(u)

    #         ###----------------------//////// CONNECTING WITH DATABASE ///////-----------------------------#

    #         result = database.update_car_and_seller_details(u)
    #         if result:
    #                 messagebox.showinfo("Message","Car & Seller details added successfully")
    #                 # self.root.destroy()
                
    #         else:
    #                 messagebox.showerror("Alert!", "Something Went wrong")

    # def open_home_page(self):
    #     self.root.destroy()
    #     n = new_mainpage.HomePage()
    #     n.homepage_widgets()

if __name__=="__main__":
    s=BoughtCarPage()
    s.new_bought_car_page_widgets()