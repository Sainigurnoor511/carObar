from tkinter import *
from PIL import ImageTk, Image

class MainPage():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("1066x600")
        self.root.title("CAR APP")

    def mainpage_widgets(self):
        self.frame = Frame(self.root, width=600, height=400, bg= "black")
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

        self.image = (Image.open("images/car.jpg")).resize((1066, 600))
        self.img = ImageTk.PhotoImage(self.image)

        self.label = Label(self.frame, image = self.img, bg="black")
        self.label.pack()

    def tkinter_menu(self):
                
        self.menubar = Menu(self.root)
        
        # Adding File Menu and commands
        self.file = Menu(self.menubar, tearoff = 0)
        self.file.add_command(label ='New File', command = None)
        self.file.add_command(label ='Open...', command = None)
        self.file.add_command(label ='Save', command = None)
        self.file.add_separator()
        
        self.menubar.add_cascade(label ='File', menu = self.file)
        self.file.add_command(label ='Exit', command = self.root.destroy)
        
        # # Adding Edit Menu and commands
        self.edit = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Edit', menu = self.edit)
        self.edit.add_command(label ='Cut', command = None)
        self.edit.add_command(label ='Copy', command = None)
        self.edit.add_command(label ='Paste', command = None)
        self.edit.add_command(label ='Select All', command = None)
        self.edit.add_separator()
        self.edit.add_command(label ='Find...', command = None)
        self.edit.add_command(label ='Find again', command = None)
        
        # # Adding Help Menu
        self.help_ = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label ='Help', menu = self.help_)
        self.help_.add_command(label ='Tk Help', command = None)
        self.help_.add_command(label ='Demo', command = None)
        self.help_.add_separator()
        self.help_.add_command(label ='About Tk', command = None)
        
        # display Menu
        self.root.config(menu = self.menubar)
    
        self.menu = Label(self.root, text = "")

        self.photo = ImageTk.PhotoImage(Image.open("images/home_button.png"))

        self.home_button = Button(self.frame, image = self.photo, width = 150, height= 40, border=0).place(x= 900, y=100)
        
        Button=canvas.create_image(380,400, image=self.photo)

    

mp = MainPage()
mp.mainpage_widgets()
mp.tkinter_menu()
mp.root.mainloop()