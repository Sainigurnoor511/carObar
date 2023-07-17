from tkinter import *
from PIL import Image, ImageTk
import login
import sv_ttk
from tkinter import ttk

class Dashboard:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1000x700")
        self.root.title("CarOBar")
        self.root.resizable(width =False, height= False)
        self.root.configure(bg ='#fff')
        sv_ttk.set_theme("light")

    def dashboard_menu(self):
        self.tmenu = Menu(self.root)

        self.home_menu = Menu(self.tmenu, tearoff=0)
        self.tmenu.add_cascade(label='Home', menu=self.home_menu)

        self.sell_menu = Menu(self.tmenu,tearoff =0)
        self.tmenu.add_cascade(label= 'Sell', menu = self.sell_menu)

        self.sell_menu.add_command(label="Sell Your Car") 
        #---------------------------------------------------------------

        self.Buy_menu = Menu(self.tmenu,tearoff =0)
        self.tmenu.add_cascade(label= 'Buy', menu = self.Buy_menu)
        # adding commands in Buy_menu
        self.Buy_menu.add_command(label="New Cars") 
        self.Buy_menu.add_command(label="Used Cars") 

        #----------------------------------------------------------------
        self.services_menu = Menu(self.tmenu,tearoff =0)
        self.tmenu.add_cascade(label= 'Services', menu = self.services_menu)

        self.services_menu.add_command(label="Car Wash") 
        self.services_menu.add_command(label="Rent Car")  
        #----------------------------------------------------------------


        self.root.config(menu=self.tmenu)

        #---------------------------------------------------------------

    def dashboard_widgets(self):
        self.b = ttk.Button(self.root, text="Login / Sign up",width=20,pady=6, background = "#57a1f8", fg ="white",border=0, command = self.open_login_window) 
        self.b.place(x=450, y=600)

        self.root.mainloop()
        
    #for importing the login window

    def open_login_window(self):
        self.root.destroy()
        lg = login.Login()
        lg.login_frame()

if __name__=="__main__":
    t = Dashboard()
    t.dashboard_menu()
    t.dashboard_widgets()