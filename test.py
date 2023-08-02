from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import database
import sv_ttk

class BuyCarPage:

    def __init__(self):
        self.root = Tk()
        self.root.title("Scrollable Frames Example")
        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width/2)-(self.width_of_window/2)
        self.y_coordinate = (self.screen_height/2)-(self.height_of_window/1.8)
        self.root.geometry("%dx%d+%d+%d" %(self.width_of_window,self.height_of_window,self.x_coordinate,self.y_coordinate))
        self.root.resizable(width =False, height= False)
        sv_ttk.set_theme("light")


        #* Create the first frame
        self.frame1 = Frame(self.root, bg="white")
        self.label1 = ttk.Label(self.frame1, text='buy car', foreground='#57A1F8', background="white", font=('Harlow Solid Italic', 40, 'normal'))
        self.label1.place(x=420, y=5)

        #! Labels and comboboxes for selecting car preferences
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.car_brand = ttk.Label(self.frame1, text='Select Brand', foreground='#57A1F8', background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.car_brand.place(x=80, y=110)

        self.car_brands = []
        for i in database.manage_cars_stock():
            self.car_brands.append(i[2])

        self.selectbrand = ttk.Combobox(self.frame1, values=self.car_brands, width=27)
        self.selectbrand['state'] = 'readonly'
        self.selectbrand.set("Select Brand")
        self.selectbrand.place(x=80, y=140)



        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.budget = ttk.Label(self.frame1, text='Select Budget', foreground='#57A1F8', background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.budget.place(x=398, y=110)

        self.selectbudget = ttk.Combobox(self.frame1, width=27)
        self.selectbudget['values'] = ( '0 - 3,00,000', 
                                        '3,00,000 - 7,00,000', 
                                        'Above 7,00,000')
        self.selectbudget['state'] = 'readonly'
        self.selectbudget.set("Select Budget")
        self.selectbudget.place(x=398, y=140)



        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.new_used = ttk.Label(self.frame1,text='New / Used', foreground='#57A1F8', background="white", font=('Harlow Solid Italic', 16, 'normal'))
        self.new_used.place(x=705, y=110)

        self.select_new_used = ttk.Combobox(self.frame1, width=27)
        self.select_new_used['values'] = ('New ','Used')
        self.select_new_used['state'] = 'readonly'
        self.select_new_used.set("Select New/Used")
        self.select_new_used.place(x=705, y=140)

        #!_________________________________________________________________________________________________________

        self.divider = ttk.Label(self.frame1,text= '__________________________________________________________________________________________________________________', width=100, foreground='black', background="white", font=('Bahnschrift SemiBold Condensed', 20, 'normal'))
        self.divider.place(x=0, y=186)

        #!_______________________________________________________________________________________________________________



        # Create the second frame as a scrollable frame
        self.canvas = Canvas(self.root, borderwidth=0, bg="white")
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame2 = Frame(self.canvas, bg="white", padx=10)
        self.label2 = ttk.Label(self.frame2, text="",background="white", font=("Helvetica", 16))
        self.label2.place(x=0, y=0)


        d = database.get_cars()
        for i in d:
            print(i)
            self.image_path = Image.open('images/Cars/Used Cars/Honda Civic.png').resize((472,270))
            self.imgTk = ImageTk.PhotoImage(self.image_path)
            self.image_label = ttk.Label(self.frame2, image=self.imgTk, background="white")
            self.image_label.place(x=0, y=0)

            self.car_type = ttk.Label(self.frame2, text= i[1], width=8, foreground='#57A1F8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_type.place(x=500, y=40)

            self.car_brand = ttk.Label(self.frame2, text= i[2], width=15, foreground='#57A1F8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_brand.place(x=500, y=90)

            self.car_model = ttk.Label(self.frame2, text= i[3], width=20, foreground='#57A1F8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_model.place(x=580, y=90)

            self.car_variant = ttk.Label(self.frame2, text= i[4], width=7, foreground='#57A1F8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_variant.place(x=500, y=140)

            self.car_mileage = ttk.Label(self.frame2, text= i[5], width=10, foreground='#57A1F8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.car_mileage.place(x=580, y=140)

            self.ownership = ttk.Label(self.frame2, text= i[6], width=25, foreground='#57A1F8', background="white", font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.ownership.place(x=690, y=140)

            self.fueltype = ttk.Label(self.frame2, text= i[7], width=7, foreground='#57A1F8', font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.fueltype.place(x=680, y=90)

            self.rto = ttk.Label(self.frame2, text= i[8], width=10, foreground='#57A1F8', font=('Bahnschrift SemiBold Condensed', 17, 'normal'))
            self.rto.place(x=500, y=190)



        # for i in range(50):
        #     # Adding some sample content to the scrollable frame
        #     ttk.Label(self.frame2, text=f"Item {i}", font=("Helvetica", 12)).pack()

        # Pack the frames into the canvas
        self.canvas.create_window((0, 0), window= self.frame2, anchor="sw", height=700, width=1000)
        self.canvas.pack(side="bottom", fill="both", expand=True)

        # Configure the canvas to update the scrollable region and handle mousewheel scrolling
        self.canvas.bind("<Configure>", self.on_configure)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Pack the scrollbar to the right side
        self.scrollbar.place(x=982, y=215, height=490)

        # Pack the first frame
        self.frame1.pack(fill="both", expand=True)


    def on_configure(self, event):
        # Update scrollable region to encompass the entire frame
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_mousewheel(self, event):
        # Scroll the canvas when the mouse wheel is used
        self.canvas.yview_scroll(-int(event.delta / 120), "units")



buy = BuyCarPage()
buy.root.mainloop()