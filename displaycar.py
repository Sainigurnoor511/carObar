from tkinter import *
from tkinter import ttk
import database
from tkinter import messagebox

class DisplayCars:
    def __init__(self):
        self.root = Tk()

        self.fullwidth = self.root.winfo_screenwidth()
        self.fullheight = self.root.winfo_screenheight()
        self.width = int((self.fullwidth - 1920) / 2)+180
        self.height = int((self.fullheight - 1080) / 2)+110
        s = "1920x1080+" + str(self.width) + "+" + str(self.height)
        self.root.geometry(s)
        # self.root.resizable(False,False)
        
        self.root.title("CARS") 

    def display_new_cars(self):
        self.f = Frame(self.root,bg="Light Yellow")
        self.f.place(x=20,y=20,width=1920,height=1080)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G"))

        self.tree_view.heading("#0",text="ID")
        self.tree_view.column("#0", anchor=CENTER,width=50)

        self.tree_view.heading("#1",text="Name")
        self.tree_view.column("#1", anchor=CENTER,width=150)

        self.tree_view.heading("#2",text="Type")
        self.tree_view.column("#2", anchor=CENTER,width=150)

        self.tree_view.heading("#3",text="Engine")
        self.tree_view.column("#3", anchor=CENTER,width=150)

        self.tree_view.heading("#4",text="Mileage")
        self.tree_view.column("#4", anchor=CENTER,width=150)

        self.tree_view.heading("#5",text="Price")
        self.tree_view.column("#5", anchor=CENTER,width=150)
        

        for i in database.display_new_car():
            self.tree_view.insert("",0,text=i[0],values=(i[1],i[2],i[3],i[4],i[5]))
        # self.tree_view.bind("<Double-Button-1>",self.perform_acions)    
        self.tree_view.place(x=10,y=10)

    # def perform_acions(self,e):
    #     # Focus Row 
    #     r = self.tree_view.focus()
    #     print(r)

    #     # Get the column id
    #     column_id = self.tree_view.identify_column(e.x)
    #     print("Column Id - ", column_id)

    #     # Get the data from the row according to the focused row
    #     d = self.tree_view.item(r)
    #     print("Focused Row - ", d)

    #     car_id = d.get("text")
    #     print("Student Id - ", car_id)
    #     d = (car_id,)

    #     if column_id == "#6":
    #         confirmation = messagebox.askyesno("Alert!","Do you really want to delete this data?")
    #         if confirmation:
    #             result = database.delete_student(d)
    #             if result:
    #                 messagebox.showinfo("Message","Student data deleted successfully")
    #                 self.root.destroy()
    #                 v = DisplayNewCar()
    #                 v.build_view_students_page_widgets()
    #             else:
    #                 messagebox.showwarning("Alert!","Something went wrong")
    #     elif column_id == "#7":
    #         print("You clicked on the update")


    def display_used_cars(self):
        self.f = Frame(self.root,bg="Light Yellow")
        self.f.place(x=20,y=20,width=1920,height=1080)

        self.tree_view = ttk.Treeview(self.f,columns=("A","B","C","D","E","F","G"))

        self.tree_view.heading("#0",text="ID")
        self.tree_view.column("#0", anchor=CENTER,width=50)

        self.tree_view.heading("#1",text="Name")
        self.tree_view.column("#1", anchor=CENTER,width=150)

        self.tree_view.heading("#2",text="Type")
        self.tree_view.column("#2", anchor=CENTER,width=150)

        self.tree_view.heading("#3",text="Engine")
        self.tree_view.column("#3", anchor=CENTER,width=150)

        self.tree_view.heading("#4",text="Mileage")
        self.tree_view.column("#4", anchor=CENTER,width=150)

        self.tree_view.heading("#5",text="Price")
        self.tree_view.column("#5", anchor=CENTER,width=150)

        

        for i in database.display_used_car():
            self.tree_view.insert("",0,text=i[0],values=(i[1],i[2],i[3],i[4],i[5]))
        # self.tree_view.bind("<Double-Button-1>",self.perform_acions)    
        self.tree_view.place(x=10,y=10)

    # def perform_acions(self,e):
    #     # Focus Row 
    #     r = self.tree_view.focus()
    #     print(r)

    #     # Get the column id
    #     column_id = self.tree_view.identify_column(e.x)
    #     print("Column Id - ", column_id)

    #     # Get the data from the row according to the focused row
    #     d = self.tree_view.item(r)
    #     print("Focused Row - ", d)

    #     car_id = d.get("text")
    #     print("Student Id - ", car_id)
    #     d = (car_id,)

    #     if column_id == "#6":
    #         confirmation = messagebox.askyesno("Alert!","Do you really want to delete this data?")
    #         if confirmation:
    #             result = database.delete_student(d)
    #             if result:
    #                 messagebox.showinfo("Message","Student data deleted successfully")
    #                 self.root.destroy()
    #                 v = DisplayNewCar()
    #                 v.build_view_students_page_widgets()
    #             else:
    #                 messagebox.showwarning("Alert!","Something went wrong")
    #     elif column_id == "#7":
    #         print("You clicked on the update")


if __name__=="__main__":
    v = DisplayCars()
    v.display_new_cars()
    v.display_used_cars()
    v.root.mainloop()