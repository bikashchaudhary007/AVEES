# using class
# Importing custome ttk
from tkinter import StringVar
import customtkinter as cttk
from Dashboard import Dashboard
import threading
import serial
import mysql.connector


db_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # Replace with your MySQL password
    database="aveesdb"
)


class LoginSystem:
    # Define serial_port as a class attribute
    serial_port = 'COM5'

    def __init__(self,root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("700x600+350+50")
        self.root.resizable(False, False)
        # self.root.config(bg="#c8c7ff")

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
        LoginFrame = cttk.CTkFrame(root, width=420, height=450, fg_color=("white", "#4B49AC"))
        LoginFrame.pack(pady=20)

        #--For Heading
        heading_title = cttk.CTkLabel(LoginFrame, text="AVE2S", font=("Arial",28,"bold")).place(x=150,y=30)
        sub_heading  = cttk.CTkLabel(LoginFrame, text="Automated Vehicle Entry and Exit System", font=("Arial",14)).place(x=80, y=60)

        login_title  = cttk.CTkLabel(LoginFrame, text="Login Here", font=("Arial",16,"bold")).place(x=150, y=100)

        #--For Username
        lbl_username  = cttk.CTkLabel(LoginFrame, text="Username", font=("Arial",14,"bold")).place(x=120, y=150)
        txt_username = cttk.CTkEntry(LoginFrame,textvariable=self.username, placeholder_text="username", fg_color="transparent", text_color=("black","white"), width=200, height=30)
        txt_username.place(x=120, y=175)

        #--For Password
        lbl_password  = cttk.CTkLabel(LoginFrame, text="Password", font=("Arial",14,"bold")).place(x=120, y=210)
        txt_password = cttk.CTkEntry(LoginFrame, placeholder_text="Password", fg_color="transparent", text_color=("black","white"), width=200, height=30, show="*")
        txt_password.place(x=120, y=235)

        btn_login = cttk.CTkButton(LoginFrame, text="Login", font=("Arial",14,"bold"),command=self.button_event, height=35, corner_radius=20)
        btn_login.place(x=120, y=285)


        #--Light and Dark Theme button
        switch_var = cttk.StringVar(value="off")
        switch = cttk.CTkSwitch(LoginFrame, text=("Theme"), command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
        switch.place(x=120, y=350)

   
    def button_event(self):
        # Hide the login window
        self.root.iconify()

        # Create and show the Dashboard window
        dashboard_root = cttk.CTk()
        dashboard_obj = Dashboard(dashboard_root, self.username.get())
        dashboard_root.protocol("WM_DELETE_WINDOW", self.on_dashboard_close)  # handle close event
        dashboard_root.mainloop()
    
    def on_dashboard_close(self):
        # Deiconify the login window when the Dashboard is closed
        self.root.deiconify()


root = cttk.CTk()
obj = LoginSystem(root)
root.mainloop()