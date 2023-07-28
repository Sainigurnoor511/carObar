from tkinter import *
from tkinter import ttk
import database, new_bought_car_page
from tkinter import messagebox
import sv_ttk
import car_services_page,sell_car_page, new_mainpage, car_services_treeview

class DisplayCars:
    def __init__(self):
        self.root = Tk()
        self.width_of_window = 1200
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.resizable(False,False)
        self.root.title("Manage Database")

        # self.root.protocol("WM_DELETE_WINDOW",self.open_home_page)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   BUTTON FRAME   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        

    def button_frame(self):

        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20, y=10, width=1160, height=120)

        self.database1 = ttk.Button(self.f,width=32, text='Manage Brand-new Cars Bought',command=self.display_brand_new_cars)
        self.database1.place(x=30, y=25)

        self.database2 = ttk.Button(self.f, width=32, text='Manage Second-hand Cars Bought', command = self.display_secondhand_cars_bought)
        self.database2.place(x=30, y=70)

        self.database3 = ttk.Button(self.f, width=24, text='Manage In Stock Cars',command = self.display_in_stock_cars )
        self.database3.place(x=290, y=25)

        self.database4 = ttk.Button(self.f, width=24, text='Manage Cars Sold',)
        self.database4.place(x=290, y=70)

        self.database5 = ttk.Button(self.f, width=24, text='Manage Car Services', command=self.display_car_services)
        self.database5.place(x=500, y=25)


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       BRAND NEW CARS TREEVIEW          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def display_brand_new_cars(self):

        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=550)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G","H"))

        self.tree_view.heading("#0",text="ID")
        self.tree_view.column("#0", width=60)

        self.tree_view.heading("#1",text="TYPE")
        self.tree_view.column("#1", width=80, anchor=CENTER)

        self.tree_view.heading("#2",text="BRAND")
        self.tree_view.column("#2", width=120, anchor=CENTER)

        self.tree_view.heading("#3",text="MODEL")
        self.tree_view.column("#3", width=120, anchor=CENTER)

        self.tree_view.heading("#4",text="VARIANT")
        self.tree_view.column("#4", width=120, anchor=CENTER)

        self.tree_view.heading("#5",text="MILEAGE")
        self.tree_view.column("#5", width=150, anchor=CENTER)

        self.tree_view.heading("#6",text="PRICE")
        self.tree_view.column("#6", width=150, anchor=CENTER)

        self.tree_view.heading("#7",text="DELETE")
        self.tree_view.column("#7", width=120, anchor=CENTER)

        self.tree_view.heading("#8",text="UPDATE")
        self.tree_view.column("#8", width=120, anchor=CENTER)
        

        for i in database.manage_brand_new_cars():
            self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5],i[6], "Delete", "Update"))
        self.tree_view.bind("<Double-Button-1>", self.perform_action1)    
        self.tree_view.place(x=15,y=20)

    def perform_action1(self, e):
        # Focus Row 
        r = self.tree_view.focus()
        print(r)

        # Get the column id
        column_id = self.tree_view.identify_column(e.x)
        print("Column ID - ", column_id)

        # Get the data from the row according to the focused row
        d = self.tree_view.item(r)
        print("Focused Row - ", d)

        car_id = d.get("text")
        print("Car ID - ", car_id)
        d = (car_id,)

        if column_id == "#7":
            confirmation = messagebox.askyesno("Alert!","Do you really want to delete this data?")
            if confirmation:
                result = database.delete_new_cars(d)
                if result:
                    messagebox.showinfo("Message","Car data deleted successfully")
                    self.root.destroy()
                    v = DisplayCars()
                    v.display_brand_new_cars()
                    v.button_frame()
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")

        elif column_id == "#8":
            confirmation = messagebox.askyesno("Alert!","Do you really want to update this data?")
            if confirmation:
                s = new_bought_car_page.BoughtCarPage(self.tree_view.item(r))
                self.root.destroy()
                s.new_bought_car_page_widgets()



#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!       IN STOCK CARS TREEVIEW         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    def display_in_stock_cars(self):

        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=550)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G","H","I","J"))

        self.tree_view.heading("#0", text="ID")
        self.tree_view.column("#0", width=50)

        self.tree_view.heading("#1",text="TYPE")
        self.tree_view.column("#1", width=80, anchor=CENTER)

        self.tree_view.heading("#2",text="BRAND")
        self.tree_view.column("#2", width=100, anchor=CENTER)

        self.tree_view.heading("#3",text="MODEL")
        self.tree_view.column("#3", width=100, anchor=CENTER)

        self.tree_view.heading("#4",text="VARIANT")
        self.tree_view.column("#4", width=100, anchor=CENTER)

        self.tree_view.heading("#5",text="KMS DRIVEN")
        self.tree_view.column("#5", width=140, anchor=CENTER)

        self.tree_view.heading("#6",text="REGISTRATION YEAR")
        self.tree_view.column("#6", width=150, anchor=CENTER)

        self.tree_view.heading("#7",text="OWNERSHIP")
        self.tree_view.column("#7", width=120, anchor=CENTER)

        self.tree_view.heading("#8",text="PRICE")
        self.tree_view.column("#8", width=100, anchor=CENTER)

        self.tree_view.heading("#9",text="DELETE")
        self.tree_view.column("#9", width=90, anchor=CENTER)

        self.tree_view.heading("#10",text="UPDATE")
        self.tree_view.column("#10", width=90, anchor=CENTER)
        

        for i in database.manage_cars_stock():
            self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], "Delete", "Update"))
        self.tree_view.bind("<Double-Button-1>", self.perform_action2)    
        self.tree_view.place(x=15,y=20)

    def perform_action2(self, e):
        # Focus Row 
        r = self.tree_view.focus()
        print(r)

        # Get the column id
        column_id = self.tree_view.identify_column(e.x)
        print("Column ID - ", column_id)

        # Get the data from the row according to the focused row
        d = self.tree_view.item(r)
        print("Focused Row - ", d)

        car_id = d.get("text")
        print("Car ID - ", car_id)
        d = (car_id,)

        if column_id == "#9":
            confirmation = messagebox.askyesno("Alert!","Do you really want to delete this data?")
            if confirmation:
                result = database.delete_cars_stock(d)
                if result:
                    messagebox.showinfo("Message","Car data deleted successfully")
                    self.root.quit()
                    v = DisplayCars()
                    v.display_in_stock_cars()
                    v.button_frame()
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")

        elif column_id == "#10":
            confirmation = messagebox.askyesno("Alert!","Do you really want to update this data?")
            if confirmation:
                s = sell_car_page.SellCarPage(self.tree_view2.item(r))
                self.root.quit()
                s.sellcar_page_widgets()


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!      CAR SERVICES          !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def display_car_services(self):
        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=525)

        self.tree_view = ttk.Treeview(self.f, columns= ("A","B","C","D","E","F","G"))

        self.tree_view.heading("#0", text="ID")
        self.tree_view.column("#0", width=70, anchor=CENTER)

        self.tree_view.heading("#1", text="SERVICE TYPE")
        self.tree_view.column("#1", width= 140, anchor=CENTER)

        self.tree_view.heading("#2", text="SERVICE TIME")
        self.tree_view.column("#2", width= 170, anchor=CENTER)

        self.tree_view.heading("#3",text= "SERVICE DATE")
        self.tree_view.column("#3", width= 150, anchor=CENTER)

        self.tree_view.heading("#4",text= "CUSTOMER NAME")
        self.tree_view.column("#4", width= 180, anchor=CENTER)

        self.tree_view.heading("#5",text= "CUSTOMER CONTACT")
        self.tree_view.column("#5", width= 160, anchor=CENTER)

        self.tree_view.heading("#6",text= "DELETE")
        self.tree_view.column("#6", width= 120, anchor=CENTER)

        self.tree_view.heading("#7",text= "UPDATE")
        self.tree_view.column("#7", width= 120, anchor=CENTER)


        for i in database.get_car_services_details():
            self.tree_view.insert("",0,text=i[0],values=(i[1],i[2],i[3],i[4],i[5],"Delete","Update"))

        self.tree_view.bind("<Double-Button-1>", self.perform_action4)
        self.tree_view.place(x=15, y=20)

    def perform_action4(self,e):
        
        #Focus Row
        r = self.tree_view.focus()
        print(r)

        #Get column id
        column_id = self.tree_view.identify_column(e.x)
        print("Column ID - ", column_id)

        #Get the data from the row acording to the focused row

        d = self.tree_view.item(r)
        print("Focused Row - ",d)


        service_id = d.get("text")
        print("Service Id - ",service_id)
        d =(service_id,)


        if column_id =="#6":
            confirmation = messagebox.askyesno("Alert!","Do you really want to delete")
            if confirmation:
                result = database.delete_car_services_data(d)
                if result:
                    messagebox.showinfo("Message","Sevices data deleted successfully")
                    self.display_car_services()
                    
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")
        
        elif column_id == "#7":
            a = car_services_page.CarServicePage(self.tree_view.item(r))
            self.root.destroy()
            a.car_services_page_widgets()    

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!         Second-Hand Cars Bought             !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    def display_secondhand_cars_bought(self):


        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20,y=150,width=1160,height=550)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G","H","I","J"))

        self.tree_view.heading("#0",text="ID")
        self.tree_view.column("#0", anchor=CENTER,width=40)

        self.tree_view.heading("#1",text="TYPE")
        self.tree_view.column("#1", anchor=CENTER,width=90)

        self.tree_view.heading("#2",text="BRAND")
        self.tree_view.column("#2", anchor=CENTER,width=100)

        self.tree_view.heading("#3",text="MODEL")
        self.tree_view.column("#3", anchor=CENTER,width=100)

        self.tree_view.heading("#4",text="VARIANT")
        self.tree_view.column("#4", anchor=CENTER,width=100)

        self.tree_view.heading("#5",text="KMS DRIVEN")
        self.tree_view.column("#5", anchor=CENTER,width=140)

        self.tree_view.heading("#6",text="REGISTRATION YEAR")
        self.tree_view.column("#6", anchor=CENTER,width=150)

        self.tree_view.heading("#7",text="OWNERSHIP")
        self.tree_view.column("#7", anchor=CENTER,width=120)

        self.tree_view.heading("#8",text="PRICE")
        self.tree_view.column("#8", anchor=CENTER,width=100)

        

        self.tree_view.heading("#9",text="DELETE")
        self.tree_view.column("#9", anchor=CENTER,width=90)

        self.tree_view.heading("#10",text="UPDATE")
        self.tree_view.column("#10", anchor=CENTER,width=90)
        

        for i in database.get_car_and_seller_details():
            self.tree_view.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], "Delete", "Update"))
        self.tree_view.bind("<Double-Button-1>", self.perform_actions4)    
        self.tree_view.place(x=15,y=20)

    def perform_actions4(self, e):
        # Focus Row 
        r = self.tree_view.focus()
        print(r)

        # Get the column id
        column_id = self.tree_view.identify_column(e.x)
        print("Column ID - ", column_id)

        # Get the data from the row according to the focused row
        d = self.tree_view.item(r)
        print("Focused Row - ", d)

        car_id = d.get("text")
        print("Car ID - ", car_id)
        d = (car_id,)

        if column_id == "#9":
            confirmation = messagebox.askyesno("Alert!","Do you really want to delete this data?")
            if confirmation:
                result = database.delete_car_and_seller_details(d)
                if result:
                    messagebox.showinfo("Message","Car data deleted successfully")
                    self.root.destroy()
                    v = DisplayCars()
                    v.display_secondhand_cars_bought()
                    v.button_frame()
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")

        elif column_id == "#10":
            confirmation = messagebox.askyesno("Alert!","Do you really want to update this data?")
            if confirmation:
                s = sell_car_page.SellCarPage(self.tree_view.item(r))
                self.root.destroy()
                s.sellcar_page_widgets()
                


    # def open_home_page(self):
    #     self.root.destroy()
    #     n = new_mainpage.HomePage()
    #     n.homepage_widgets() 

if __name__=="__main__":
    v = DisplayCars()
    v.button_frame()
    v.root.mainloop()