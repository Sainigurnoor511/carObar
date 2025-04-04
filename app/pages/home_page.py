import customtkinter as ctk
from PIL import Image
from app.pages import (
    buy_car_page,
    sell_car_page,
    new_bought_car_page,
    car_services_page,
    manage_catalogue_page,
    invoice_generator_page,
    update_password_page,
)

class HomePage:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.iconbitmap("app/assets/myIcon.ico")
        self.root.title("carObar")

        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 1.8)
        self.root.geometry(f"{self.width_of_window}x{self.height_of_window}+{int(self.x_coordinate)}+{int(self.y_coordinate)}")
        self.root.resizable(width=False, height=False)

    def homepage_widgets(self):
        self.mainframe = ctk.CTkFrame(self.root, width=1000, height=700, fg_color="white")
        self.mainframe.place(x=0, y=0)

        self.bg_image = ctk.CTkImage(light_image=Image.open("app/assets/background.jpg"), size=(1000, 564))
        self.background_pic = ctk.CTkLabel(self.mainframe, image=self.bg_image, text="")
        self.background_pic.place(x=-2, y=136)

        self.heading = ctk.CTkLabel(self.mainframe, text="Welcome Administrator!", text_color="#1C1C1C", fg_color="white", font=("Bahnschrift SemiCondensed", 35))
        self.heading.place(x=280, y=30)

        self.sidebar_img = ctk.CTkImage(light_image=Image.open("app/assets/home_page/sidebar.png"), size=(45, 45))
        self.sidebar_button = ctk.CTkButton(self.mainframe, image=self.sidebar_img, text="", fg_color="white", hover=False, command=self.open_sidebar)
        self.sidebar_button.place(x=10, y=35)

        self.user_img = ctk.CTkImage(light_image=Image.open("app/assets/home_page/user.png"), size=(45, 45))
        self.user_label = ctk.CTkLabel(self.mainframe, image=self.user_img, fg_color="white", text="")
        self.user_label.place(x=940, y=35)

        self.context_menu = ctk.CTkOptionMenu(self.mainframe, values=["Update Password"], command=self.menu_action)
        self.user_label.bind("<Button-3>", self.show_context_menu)

    def show_context_menu(self, event):
        self.context_menu.place(x=event.x_root, y=event.y_root)

    def menu_action(self, option):
        if option == "Update Password":
            up = update_password_page.UpdatePass()
            up.update_passw_frame()

    def open_sidebar(self):
        self.sidebar_frame = ctk.CTkFrame(self.root, height=700, width=200, fg_color="black")
        self.sidebar_frame.place(x=0, y=0)

        self.heading = ctk.CTkLabel(self.sidebar_frame, text="carObar", text_color="white", fg_color="black", font=("Magneto", 23))
        self.heading.place(x=40, y=30)

        self.back_img = ctk.CTkImage(light_image=Image.open("app/assets/home_page/back.png"), size=(20, 20))
        self.back_button = ctk.CTkButton(self.sidebar_frame, image=self.back_img, text="", fg_color="black", hover=False, command=self.close_sidebar)
        self.back_button.place(x=10, y=42)

        sidebar_buttons = [
            ("app/assets/home_page/dashboard.png", self.open_dashboard, 150),
            ("app/assets/home_page/buycar.png", self.open_buycar, 200),
            ("app/assets/home_page/sellcar.png", self.open_sellcar, 250),
            ("app/assets/home_page/services.png", self.open_car_services, 300),
            ("app/assets/home_page/exit.png", self.exit_button, 350),
        ]

        for img_path, command, y in sidebar_buttons:
            img = ctk.CTkImage(light_image=Image.open(img_path), size=(150, 30))
            btn = ctk.CTkButton(self.sidebar_frame, image=img, text="", fg_color="black", hover=False, command=command)
            btn.image = img
            btn.place(x=25, y=y)

    def close_sidebar(self):
        self.sidebar_frame.destroy()

    def open_dashboard(self):
        self.dashboard_frame = ctk.CTkFrame(self.root, width=1000, height=700, fg_color="white")
        self.dashboard_frame.place(x=0, y=100)
        self.close_sidebar()

        self.dashboard_buttons_img = ctk.CTkImage(light_image=Image.open("app/assets/home_page/dashboard_buttons.png"))
        self.dashboard_buttons = ctk.CTkLabel(self.dashboard_frame, image=self.dashboard_buttons_img, text="", fg_color="white")
        self.dashboard_buttons.place(x=10, y=50)

        self.graph_img = ctk.CTkImage(light_image=Image.open("app/assets/home_page/graph.png"), size=(478, 400))
        self.graph_image = ctk.CTkLabel(self.dashboard_frame, image=self.graph_img, text="", fg_color="white")
        self.graph_image.place(x=520, y=195)

        labels = [
            ("₹ 2.5 cr", "#01FB09", (42, 80)),
            ("926", "#FE0101", (325, 80)),
            ("10", "#FFCF00", (546, 70)),
            ("10", "#0079C6", (799, 70)),
        ]

        for text, color, (x, y) in labels:
            lbl = ctk.CTkLabel(self.dashboard_frame, text=text, text_color=color, font=("Montserrat Medium", 25, "bold"), fg_color="white")
            lbl.place(x=x, y=y)

        self.new_bought_car_button = ctk.CTkButton(self.root, text="Add New Cars", command=self.open_new_bought_car)
        self.new_bought_car_button.place(x=60, y=340)

        self.manage_database_button = ctk.CTkButton(self.root, text="Manage Database", command=self.open_manage_database)
        self.manage_database_button.place(x=60, y=400)

        self.generate_invoice_button = ctk.CTkButton(self.root, text="Generate Invoice", command=self.open_invoice_generator)
        self.generate_invoice_button.place(x=60, y=460)

    def open_buycar(self):
        self.root.destroy()
        buy_car_page.BuyCarPage()

    def open_sellcar(self):
        self.root.destroy()
        sell_car_page.SellCarPage().sellcar_page_widgets()

    def open_car_services(self):
        car_services_page.CarServicePage().car_services_page_widgets()

    def open_manage_database(self):
        self.root.destroy()
        manage_catalogue_page.DisplayCars().button_frame()

    def open_new_bought_car(self):
        self.root.destroy()
        new_bought_car_page.BoughtCarPage().new_bought_car_page_widgets()

    def open_invoice_generator(self):
        invoice_generator_page.InvoiceGenerator().widgets()

    def exit_button(self):
        self.root.destroy()

if __name__ == "__main__":
    hm = HomePage()
    hm.homepage_widgets()
    hm.root.mainloop()
