from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class HomePage:
    def __init__(self):
        self.root = Tk()
        # self.root.geometry('1000x700')
        self.root.title('Home Page')

        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))


    def homepage_widgets(self):

        # Main Frame
        self.mainframe = Frame(self.root, width=1000, height=700, background="#1C1C1C")
        self.mainframe.place(x=0, y=0)

        self.heading = ttk.Label(self.mainframe, text='Welcome Administrator !', foreground='white',background="#1C1C1C", font=('Bahnschrift SemiCondensed', 30, 'normal'))
        self.heading.place(x=320, y=20)

        self.image_path = Image.open('assets/frame0/sidebar.png').resize((40,40))
        self.sidebar_image = ImageTk.PhotoImage(self.image_path)
        self.sidebar_button = Button(self.mainframe, image= self.sidebar_image, border=0, background="#1C1C1C", command= self.open_side_bar)
        self.sidebar_button.place(x=20,y=30)

    def open_side_bar(self):
        # Sidebar/Menubar for accessing different windows
        self.sidebar_frame = Frame(self.root, height=700, width=200, background= 'black')
        self.sidebar_frame.place(x=0, y=0)

        self.heading = ttk.Label(self.sidebar_frame, text='carObar', foreground='white',background="black", font=('Magneto', 23, 'normal'))
        self.heading.place(x=40, y=30)

        self.image_path = Image.open('assets/frame0/back.png').resize((20,20))
        self.back_image = ImageTk.PhotoImage(self.image_path)
        self.back_button = Button(self.sidebar_frame, image= self.back_image, border=0, background="black",command= self.close_sidebar)
        self.back_button.place(x=10,y=45)

        self.image_path = Image.open('assets/frame0/dashboard.png').resize((140,40))
        self.dashboard_image = ImageTk.PhotoImage(self.image_path)
        self.dashboard_button = Button(self.sidebar_frame, image= self.dashboard_image, border=0, background="black", command= self.open_dashboard)
        self.dashboard_button.place(x=35,y=100)

    def close_sidebar(self):
        self.sidebar_frame.destroy()

    def open_dashboard(self):

        self.dashboard_frame = Frame(self.root, width=800, height=600, background= '#1C1C1C')
        self.dashboard_frame.place(x=200, y=100)





if __name__ == '__main__':
    hm = HomePage()
    hm.homepage_widgets()
    hm.root.mainloop()