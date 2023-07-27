from tkinter import *
from tkinter import ttk
import database, car_services_page
from tkinter import messagebox


class Services:
    def __init__(self):
        self.root = Tk()
        self.width_of_window = 1200
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.resizable(width =False, height= False)
        self.root.title("Services Details")


    def display_car_services(self):
        self.f2 = Frame(self.root, background="light blue")
        self.f2.place(x=20,y=150,width=1160,height=525)

        self.tree_view = ttk.Treeview(self.f2, columns= ("A","B","C","D","E","F","G"))

        self.tree_view.heading("#0",text= "ID")
        self.tree_view.column("#0", width= 80, anchor=CENTER)

        self.tree_view.heading("#1",text= "SERVICE TYPE")
        self.tree_view.column("#1", width= 140,anchor="center")

        self.tree_view.heading("#2",text= "SERVICE TIME")
        self.tree_view.column("#2", width= 170,anchor="center")

        self.tree_view.heading("#3",text= "SERVICE DATE")
        self.tree_view.column("#3", width= 150,anchor="center")

        self.tree_view.heading("#4",text= "CUSTOMER NAME")
        self.tree_view.column("#4", width= 180,anchor="center")

        self.tree_view.heading("#5",text= "CUSTOMER CONTACT")
        self.tree_view.column("#5", width= 160,anchor="center")

        self.tree_view.heading("#6",text= "DELETE")
        self.tree_view.column("#6", width= 120,anchor="center")

        self.tree_view.heading("#7",text= "UPDATE")
        self.tree_view.column("#7", width= 120,anchor="center")


        for i in database.get_car_services_details():
            self.tree_view.insert("",0,text=i[0],values=(i[1],i[2],i[3],i[4],i[5],"Delete","Update"))

        self.tree_view.bind("<Double-Button-1>", self.perform_action)
        self.tree_view.place(x=15, y=20)

    def perform_action(self,e):
        
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
        

if __name__=="__main__":
    
    v = Services()
    v.display_car_services()
    v.root.mainloop()