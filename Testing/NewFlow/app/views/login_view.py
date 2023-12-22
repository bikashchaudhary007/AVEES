# views/login_view.py
from tkinter import StringVar
import tkinter as tk
import customtkinter as cttk
from tkinter import messagebox


class LoginView(cttk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Login Page")
        self.geometry("700x600+350+50")
        self.resizable(False, False)
        self.username = StringVar()


        cttk.set_appearance_mode("light")  # Modes: system (default), light, dark
        cttk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

        #---Dark Light theme btn
        def switch_event():
            print("switch toggled, current value:", switch_var.get())
            if(switch_var.get()=="on"):
                cttk.set_appearance_mode("dark") 
            else:
                cttk.set_appearance_mode("light")


        #Creating Login Frame
        LoginFrame = cttk.CTkFrame(self, width=420, height=450, fg_color=("white", "#4B49AC"))
        LoginFrame.pack(pady=20)

        #--For Heading
        heading_title = cttk.CTkLabel(LoginFrame, text="AVE2S", font=("Arial",28,"bold")).place(x=150,y=30)
        sub_heading  = cttk.CTkLabel(LoginFrame, text="Automated Vehicle Entry and Exit System", font=("Arial",14)).place(x=80, y=60)

        login_title  = cttk.CTkLabel(LoginFrame, text="Login Here", font=("Arial",16,"bold")).place(x=150, y=100)

         #--For Username
        self.lbl_username  = cttk.CTkLabel(LoginFrame, text="Username", font=("Arial",14,"bold")).place(x=120, y=150)
        self.txt_username = cttk.CTkEntry(LoginFrame,textvariable=self.username, placeholder_text="username", fg_color="transparent", text_color=("black","white"), width=200, height=30)
        self.txt_username.place(x=120, y=175)

        # #--For Password
        self.lbl_password  = cttk.CTkLabel(LoginFrame, text="Password", font=("Arial",14,"bold")).place(x=120, y=210)
        self.txt_password = cttk.CTkEntry(LoginFrame, placeholder_text="Password", fg_color="transparent", text_color=("black","white"), width=200, height=30, show="*")
        self.txt_password.place(x=120, y=235)


        # #Login Buttton
        btn_login = cttk.CTkButton(LoginFrame, text="Login", font=("Arial",14,"bold"),command=self.handle_login, height=35, corner_radius=20)
        btn_login.place(x=120, y=285)


        #--Light and Dark Theme button
        switch_var = cttk.StringVar(value="off")
        switch = cttk.CTkSwitch(LoginFrame, text=("Theme"), command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
        switch.place(x=120, y=350)

        

    def handle_login(self):
        username = self.txt_username.get()
        password = self.txt_password.get()

        if self.controller.authenticate_user(username, password):
            messagebox.showinfo("Login Successful", "Welcome!")
            self.destroy()
            # Add logic to open the dashboard or next view here
            self.controller.show_dashboard()  # Show the dashboard on successful login
        else:
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")
