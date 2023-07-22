import sv_ttk
import tkinter
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox
import database
# from PIL import Image, ImageTk


class CarServicePage:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("900x450")
        self.root.title("CarOBar -- Services")
        self.root.resizable(width=False, height=False)
        sv_ttk.set_theme("light")

    def car_services_page_widgets(self):

        self.frame = tkinter.Frame(self.root, width=1000, height=700)
        self.frame.place(x=0, y=0)

        self.heading = ttk.Label(self.frame, text='Services', foreground='#57A1F8', font=('Harlow Solid Italic', 40, 'normal'))
        self.heading.place(x=400, y=5)

        self.heading = ttk.Label(self.frame, text='* closed on Sunday', foreground='red')
        self.heading.place(x=705, y=175)

        #!_________________________________________________________________________________________________________


        self.customer_name = ttk.Label(self.frame,text='Customer Name', width=27, foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.customer_name.place(x=80, y=200)

        self.customer_name_entry = ttk.Entry(self.frame)
        self.customer_name_entry.place(x=80,y=250,width=200)

        self.customer_contact = ttk.Label(self.frame,text='Customer Contact', width=27, foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.customer_contact.place(x=398, y=200)

        self.customer_contact_entry = ttk.Entry(self.frame)
        self.customer_contact_entry.place(x=398,y=250,width=200)
        

        #!_________________________________________________________________________________________________________

        self.services_label = ttk.Label(self.frame,text='Select Service', width=27, foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.services_label.place(x=80, y=110)

        self.services_cb = ttk.Combobox(self.root, width=27)
        self.services_cb['values'] = (  ' Car Wash', 
                                        ' Repair', 
                                        ' Full Car Service')
        self.services_cb['state'] = 'readonly'
        self.services_cb.set("Select Service")
        self.services_cb.place(x=80, y=140)

        #!_________________________________________________________________________________________________________

        self.time_label = ttk.Label(self.frame,text='Select Time', width=27, foreground='#57A1F8', font=('Harlow Solid Italic', 16, 'normal'))
        self.time_label.place(x=398, y=110)

        self.time_cb = ttk.Combobox(self.root, width=27)
        self.time_cb['values'] = ( '9:00 am - 11:00 am', 
                                    '11:00 am - 1:00 pm', 
                                    '1:00 pm - 3:00 pm',
                                    '3:00 pm - 5:00 pm')
        self.time_cb['state'] = 'readonly'
        self.time_cb.set("Select Time")
        self.time_cb.place(x=398, y=140)

        #!_________________________________________________________________________________________________________

        self.date_label = ttk.Label(self.frame,text='Select date', width=27, foreground='#57A1F8',font=('Harlow Solid Italic', 16, 'normal'))
        self.date_label.place(x=705, y=110)

        #!_________________________________________________________________________________________________________

        self.d = DateEntry(self.root)
        self.d.place(x=705,y=140)
        # self.d.pack()

        self.book = tkinter.Button(self.root,width=12,text='Book',bg="#57A1F8",fg="white",command= self.get_services_data)
        self.book.place(x=420,y=350)
        
        #!_________________________________________________________________________________________________________

    def get_services_data(self):
        if self.services_cb.get() == "Select Service":
            messagebox.showwarning("Alert!","Please select the service")

        elif self.time_cb.get() == "Select Time" :
            messagebox.showwarning("Alert!","Please select time slot")

        elif self.d.get() == "":
            messagebox.showwarning("Alert!","Please Select the date") 

        elif self.customer_contact_entry.get()=="":
            messagebox.showwarning("Alert!","please enter the customer name")     

        elif self.customer_name_entry.get()=="":
            messagebox.showwarning("Alert!","Please enter the customer name")

        else:
            service =  self.services_cb.get()
            time = self.time_cb.get()
            Date_entry =  self.d.get()
            customerName = self.customer_name_entry.get()
            customerContact = self.customer_contact_entry.get()

            a = (service,time,Date_entry,customerName,customerContact)
        
            result = database.add_car_services_details(a)
            if result:
                    messagebox.showinfo("Message","Car Service detail added successfully")
                    self.root.destroy()
                
            else:
                    messagebox.showerror("Alert!", "Something Went wrong")




if __name__ == "__main__":
    cs = CarServicePage()
    cs.car_services_page_widgets()
    cs.root.mainloop()