import customtkinter as ctk
from tkinter import messagebox
from app.database import database
from app.pages import home_page

class Login:
    def __init__(self):
        ctk.set_appearance_mode("light")  # "dark" or "light"
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("carObar - Login Page")
        self.root.iconbitmap("app/assets/myIcon.ico")  # Icon
        self.width_of_window = 1000
        self.height_of_window = 700
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coordinate = (self.screen_width / 2) - (self.width_of_window / 2)
        self.y_coordinate = (self.screen_height / 2) - (self.height_of_window / 2)
        self.root.geometry(f"{self.width_of_window}x{self.height_of_window}+{int(self.x_coordinate)}+{int(self.y_coordinate)}")
        self.root.configure(bg='#f5f5f5')
        self.root.resizable(width=False, height=False)
        self.root.overrideredirect(1)  # Remove title bar

    def login_frame(self):
        # Centered login frame
        self.frame = ctk.CTkFrame(self.root, width=350, height=280, fg_color="white", corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        self.heading = ctk.CTkLabel(self.frame, text='Log in', text_color='#57a1f8', fg_color="white", font=('Microsoft YaHei UI Light', 18, 'bold'))
        self.heading.place(relx=0.5, rely=0.1, anchor="center")

        # --- Username Entry ---
        self.user = ctk.CTkEntry(self.frame, width=250, height=40, fg_color="white", border_width=2, corner_radius=10, text_color="black", placeholder_text="Username")
        self.user.place(relx=0.5, rely=0.3, anchor="center")
        self.user.bind('<Return>', lambda e: self.passwd.focus())  # Move to password on Enter

        # --- Password Entry ---
        self.passwd = ctk.CTkEntry(self.frame, width=250, height=40, fg_color="white", border_width=2, corner_radius=10, text_color="black", placeholder_text="Password", show="*")
        self.passwd.place(relx=0.5, rely=0.5, anchor="center")
        self.passwd.bind('<Return>', lambda e: self.log_in())  # Trigger login on Enter

        # --- Login Button ---
        self.b1 = ctk.CTkButton(self.frame, text="Sign in", fg_color='#57a1f8', text_color='white', corner_radius=10, command=self.log_in, width=250, height=40)
        self.b1.place(relx=0.5, rely=0.7, anchor="center")

        self.root.mainloop()

    def log_in(self, event=None):
        if self.user.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter the username")
            self.user.focus()
            return

        if self.passwd.get().strip() == "":
            messagebox.showwarning("Alert!", "Please enter the password")
            self.passwd.focus()
            return

        Username = self.user.get()
        password = self.passwd.get()
        credentials = (Username, password)

        result = database.register_data(credentials)
        if result:
            self.root.destroy()  # Close the login window

            # Launch the HomePage
            np = home_page.HomePage()
            np.homepage_widgets()
            np.root.mainloop()  # <-- This is required to show the HomePage window
        else:
            messagebox.showerror("Alert!", "Incorrect username & password")


if __name__ == "__main__":
    t = Login()
    t.login_frame()
