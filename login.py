from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class Login:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("925x500+300+200")
        self.root.configure(bg ='#fff')
        self.root.title("Login Page")
        self.root.resizable(width =False, height= False)
    
    def sign_in(self):
        self.Username = self.user.get()
        self.password = self.passwd.get()

        if self.Username =='admin' and self.password =='1234':
            self.screen = Toplevel(self.root)
            self.screen.title("App")
            self.screen.geometry("925x500+300+200")
            self.screen.config(bg='white')

            self.l = Label(self.screen,text="Hello World!",bg='#fff',font= ('Calibri(Body)',50,'bold')).pack(expand=True)
            self.screen.mainloop()

        elif self.Username!='admin' and self.password!='1234':
            messagebox.showerror("Invalid", "invalid username and password")
        elif  self.password!='1234':
            messagebox.showerror("Invalid", "invalid password")
        elif  self.Username!='admin':
            messagebox.showerror("Invalid", "invalid username")

        

    def login_frame(self):
        self.image_path = Image.open('images/main.png').resize((350,300))
        self.imgTk = ImageTk.PhotoImage(self.image_path)
        self.image_label = Label(self.root, image=self.imgTk, width=350, height=300,bg='white')
        self.image_label.place(x=50, y=80)
        

        self.frame = Frame(self.root,width=350,height=350,bg='white')
        self.frame.place(x=480,y=70)

        self.heading = Label(self.frame,text ='sign in' , fg='#57a1f8',bg = 'white',font=('Microsoft YaHei UI Light',23,'bold'))
        self.heading.place(x=100,y=5)
        #------------------------------------------------------------
       
        def on_enter(e):
            self.user.delete(0,'end')

        def on_leave(name):
            name == self.user.get()
            if name=='':
                self.user.insert(0,'Username')
                
        self.user = Entry(self.frame,width =25,fg ='black',border=0,font=('Microsoft YaHei UI Light',11))
        self.user.place(x=30,y=80)
        self.user.insert(0,'Username')
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=107)

        #---------------------------------------------------------

        def on_enter(e):
            self.passwd.delete(0,'end')

        def on_leave(name):
            name == self.user.get()
            if name=='':
                self.passwd.insert(0,'Password')

        self.passwd = Entry(self.frame,width =25,fg ='black',border=0,font=('Microsoft YaHei UI Light',11))
        self.passwd.place(x=30,y=150)
        self.passwd.insert(0,'Password')
        self.passwd.bind('<FocusIn>', on_enter)
        self.passwd.bind('<FocusOut>', on_leave)
        Frame(self.frame,width=295,height=2,bg='black').place(x=25,y=177)

        #------------------------------------------------------------
            
        self.b1 = Button(self.frame,width =39,pady=7,text="Sign in",bg='#57a1f8',fg='white',border=0, command=self.sign_in).place(x=35,y=204)

    #     self.label = Label(self.frame, text=" Don't have an account?",fg='black', bg ='white', font=('Microsoft YaHei UI Light',9))
    #     self.label.place(x=75,y=270)

    #     self.sign_up = Button(self.frame,width=6,text='Sign up', border=0,bg='white',cursor='hand2',fg='#57a1f8',command=self.open_sign_up_window)
    #     self.sign_up.place(x=215,y=270)

        self.root.mainloop()

    # def open_sign_up_window(self):

    #     self.root.destroy()
    #     S_up = sign_up.Signup()
    #     S_up.signup_frame()

if __name__ == "__main__":
    t = Login()
    t.login_frame()