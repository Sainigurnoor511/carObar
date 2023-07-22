from tkinter import *
from tkinter import ttk
import database, car_services_page
from tkinter import messagebox


class Services:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x600")
        self.root.resizable(width =False, height= False)
        self.root.title("Services Details")
        self.root.configure(bg='#fff')

    def build_view_services_page_widgets(self):
        self.f = Frame(self.root, bg ="#57A1F8")
        self.f.place(x=0,y=0,width =1000, height=600)

        self.tree_view = ttk.Treeview(self.f, columns= ("A","B","C","D","E","F","G","H"))

        self.tree_view.heading("#0",text= "ID")
        self.tree_view.column("#0", width= 100,anchor="center")

        self.tree_view.heading("#1",text= "Service Type")
        self.tree_view.column("#1", width= 150,anchor="center")

        self.tree_view.heading("#2",text= "Service Time")
        self.tree_view.column("#2", width= 150,anchor="center")

        self.tree_view.heading("#3",text= "Service Date")
        self.tree_view.column("#3", width= 130,anchor="center")

        self.tree_view.heading("#4",text= "Customer Name")
        self.tree_view.column("#4", width= 140,anchor="center")

        self.tree_view.heading("#5",text= "Customer Contact")
        self.tree_view.column("#5", width= 130,anchor="center")

        self.tree_view.heading("#6",text= "Delete")
        self.tree_view.column("#6", width= 100,anchor="center")

        self.tree_view.heading("#7",text= "Update")
        self.tree_view.column("#7", width= 100,anchor="center")


        for i in database.get_car_services_details():
            self.tree_view.insert("",0,text=i[0],values=(i[1],i[2],i[3],i[4],i[5],"Delete","Update"))

        self.tree_view.bind("<Double-Button-1>", self.perform_actions )
        self.tree_view.place(x=0, y=0,width=1000,height=600)
        


        self.root.mainloop()

    def perform_actions(self,e):
        
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
                    self.root.destroy()
                    v = Services()
                    v.build_view_services_page_widgets()
                    
                else:
                    messagebox.showwarning("Alert!","Something went wrong")
        
        elif column_id == "#7":
            a = car_services_page.CarServicePage(self.tree_view.item(r))
            self.root.destroy()
            a.car_services_page_widgets()
        

        









        
if __name__=="__main__":
    
    v = Services()
    v.build_view_services_page_widgets()
