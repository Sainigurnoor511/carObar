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


        

if __name__=="__main__":
    
    v = Services()
    v.display_car_services()
    v.root.mainloop()