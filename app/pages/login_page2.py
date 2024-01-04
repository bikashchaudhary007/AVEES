import tkinter as tk
from tkinter import messagebox
# Import the DashboardPage class
from pages.Dashboard2 import Dashboard  # Update the import path based on your file structure
# using class
# Importing custome ttk
from tkinter import StringVar
from tkinter import messagebox
import customtkinter as cttk
import threading
import serial
import mysql.connector
import tkinter as tk
from database.database_manager import DatabaseManager  # Importing DatabaseManager class from the database_manager module


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
        self.password = StringVar()

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
        txt_password = cttk.CTkEntry(LoginFrame, textvariable=self.password,placeholder_text="Password", fg_color="transparent", text_color=("black","white"), width=200, height=30, show="*")
        txt_password.place(x=120, y=235)

        btn_login = cttk.CTkButton(LoginFrame, text="Login", font=("Arial",14,"bold"),command=self.button_event, height=35, corner_radius=20)
        btn_login.place(x=120, y=285)


        #--Light and Dark Theme button
        switch_var = cttk.StringVar(value="off")
        switch = cttk.CTkSwitch(LoginFrame, text=("Theme"), command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
        switch.place(x=120, y=350)

   
    def button_event(self):
        # Check username and password
        if self.validate_login(self.username.get(), self.password.get()):
            # Show successful login message
            messagebox.showinfo("Login Successful", "Welcome!")
            # If login is successful, hide the login window
            self.root.iconify()
            # self.root.destroy()
            # Create and show the Dashboard window
            # dashboard_root = tk.Tk()
            # dashboard_root = cttk.CTk()
            dashboard_root = cttk.CTk()
            dashboard_obj = Dashboard(dashboard_root, self.username.get())
            dashboard_root.protocol("WM_DELETE_WINDOW", self.on_dashboard_close)  # handle close event
            dashboard_root.mainloop()
            
        else:
            # If login fails, show an error message or handle accordingly
            messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")
            # If login fails, show an error message or handle accordingly
            print("Invalid credentials. Please try again.")
    
    def on_dashboard_close(self):
        # Deiconify the login window when the Dashboard is closed
        self.root.deiconify()
    

    def validate_login(self, username, password):
        try:
            cursor = db_conn.cursor()

            # Query to check if the provided username and password exist in the database
            query = "SELECT * FROM user WHERE username = %s AND pwd = %s"
            cursor.execute(query, (username, password))
            user = cursor.fetchone()

            if user:
                # If user exists with provided credentials
                return True
            else:
                # If user doesn't exist or credentials are incorrect
                return False
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()


root = cttk.CTk()
obj = LoginSystem(root)
root.mainloop()