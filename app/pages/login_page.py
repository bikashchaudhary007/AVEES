import tkinter as tk
from tkinter import messagebox
# Import the DashboardPage class
from pages.dashboard_page import DashboardPage  # Update the import path based on your file structure

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")

        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.password_label = tk.Label(self.root, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.root, text="Login", command=self.validate_login)
        self.login_button.pack()

    def validate_login(self):
        # Get username and password entered by the user
        username = self.username_entry.get()
        password = self.password_entry.get()

        # For demo purposes, hardcoded username and password
        valid_username = "admin"
        valid_password = "admin"

        if username == valid_username and password == valid_password:
            # If credentials are valid, show a message and perform further actions (redirect to dashboard, etc.)
            messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
            self.root.destroy()  # Close the login window
            # Perform actions after successful login, e.g., navigate to DashboardPage
            # Add your logic here
            # Open the DashboardPage or perform other actions after successful login
            self.open_dashboard_page()
        else:
            messagebox.showerror("Login Error", "Invalid username or password. Try again.")
    
    def open_dashboard_page(self):
        # Instantiate the DashboardPage window
        dashboard_root = tk.Tk()
        dashboard = DashboardPage(dashboard_root)
        dashboard_root.mainloop()
