from tkinter import *
from tkinter import ttk
import database
from tkinter import messagebox
import sv_ttk

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
        

    def button_frame(self):

        self.f = Frame(self.root, background="light blue")
        self.f.place(x=20, y=10, width=1160, height=100)

        self.database1 = ttk.Button(self.f, width=35, text='Manage New Cars Bought', command=self.display_cars)
        self.database1.place(x=50, y=50)

        # self.database2 = ttk.Button(self.f, width=35, text='Manage Second-hand Cars Bought', command=self.display_sellcars)
        # self.database2.place(x=330, y=50)

        self.database3 = ttk.Button(self.f, width=35, text='Manage In Stock Cars', command=self.display_cars)
        self.database3.place(x=610, y=50)

        self.database4 = ttk.Button(self.f, width=35, text='Manage Cars Sold', command=self.display_cars)
        self.database4.place(x=890, y=50)



    def display_cars(self):

        self.car_frame = Frame(self.root, background="light blue")
        self.car_frame.place(x=20,y=130,width=1160,height=550)

        self.tree_view2 = ttk.Treeview(self.car_frame,columns=("A","B","C","D","E","F","G","H","I","J"))

        self.tree_view2.heading("#0",text="ID")
        self.tree_view2.column("#0", anchor=CENTER,width=40)

        self.tree_view2.heading("#1",text="TYPE")
        self.tree_view2.column("#1", anchor=CENTER,width=90)

        self.tree_view2.heading("#2",text="BRAND")
        self.tree_view2.column("#2", anchor=CENTER,width=100)

        self.tree_view2.heading("#3",text="MODEL")
        self.tree_view2.column("#3", anchor=CENTER,width=100)

        self.tree_view2.heading("#4",text="VARIANT")
        self.tree_view2.column("#4", anchor=CENTER,width=100)

        self.tree_view2.heading("#5",text="KMS DRIVEN")
        self.tree_view2.column("#5", anchor=CENTER,width=140)

        self.tree_view2.heading("#6",text="REGISTRATION YEAR")
        self.tree_view2.column("#6", anchor=CENTER,width=150)

        self.tree_view2.heading("#7",text="OWNERSHIP")
        self.tree_view2.column("#7", anchor=CENTER,width=120)

        self.tree_view2.heading("#8",text="PRICE")
        self.tree_view2.column("#8", anchor=CENTER,width=100)

        self.tree_view2.heading("#9",text="DELETE")
        self.tree_view2.column("#9", anchor=CENTER,width=90)

        self.tree_view2.heading("#10",text="UPDATE")
        self.tree_view2.column("#10", anchor=CENTER,width=90)
        

        for i in database.manage_cars():
            self.tree_view2.insert("",0,text = i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], "Delete", "Update"))
        self.tree_view2.bind("<Double-Button-1>", self.perform_actions2)    
        self.tree_view2.place(x=10,y=10)

    def perform_actions2(self, e):
        # Focus Row 
        r = self.tree_view2.focus()
        print(r)

        # Get the column id
        column_id = self.tree_view2.identify_column(e.x)
        print("Column ID - ", column_id)

        # Get the data from the row according to the focused row
        d = self.tree_view2.item(r)
        print("Focused Row - ", d)

        car_id = d.get("text")
        print("Car ID - ", car_id)
        d = (car_id,)

        if column_id == "#9":
            confirmation = messagebox.askyesno("Alert!","Do you really want to delete this data?")
            if confirmation:
                result = database.delete_cars(d)
                if result:
                    messagebox.showinfo("Message","Student data deleted successfully")
                    self.root.quit()
                    v = DisplayCars()
                    v.display_cars()
                    v.button_frame()
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")

        elif column_id == "#10":
            confirmation = messagebox.askyesno("Alert!","Do you really want to update this data?")
            if confirmation:
                s = Sell_car.Sellcar(self.tree_view2.item(r))
                self.root.quit()
                s.sellcar_widgets()


if __name__=="__main__":
    v = DisplayCars()
    v.display_cars()
    v.button_frame()
    v.root.mainloop()