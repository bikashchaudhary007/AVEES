import os
import customtkinter as cttk

class Dashboard:
    def __init__(self, root, user):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("700x600+350+50")
        self.root.resizable(False, False)
        self.user = user

        # Displaying the username on the dashboard
        username_label = cttk.CTkLabel(root, text=f"Welcome, {self.user}!", font=("Arial", 16, "bold"))
        username_label.pack(pady=20)

        btn_logout = cttk.CTkButton(root, text="Logout", font=("Arial",14,"bold"),command=self.logout, height=35, corner_radius=20)
        btn_logout.place(x=120, y=285)

    
    def logout(self):
     self.root.destroy()
    #  import LoginPage
     os.system("python LoginPage.py") #better to use this
     print("logout")
    
# # Usage example
# root = cttk.CTk()
# dashboard_obj = Dashboard(root)
# root.mainloop()
