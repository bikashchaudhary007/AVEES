import os
import customtkinter as cttk

class Dashboard:
    def __init__(self, root, user):
        self.root = root
        self.root.title("Dashboard")
        self.root.geometry("1280x1080+50+0")
        self.root.resizable(False, False)
        self.user = user


        # Create frames for dashboard, settings, and components
        self.dashboard_frame = cttk.CTkFrame(root, width=850, height=450, fg_color=("white", "#4B49AC"))
        self.settings_frame = cttk.CTkFrame(root, width=850, height=450, fg_color=("white", "#4B49AC"))
        self.components_frame = cttk.CTkFrame(root, width=850, height=450, fg_color=("white", "#4B49AC"))

        # Initial frame to show is the dashboard frame
        self.current_frame = self.dashboard_frame
        self.show_frame()

        # Displaying the username on the dashboard
        username_label = cttk.CTkLabel(self.dashboard_frame, text=f"Welcome, {self.user}!", font=("Arial", 16, "bold"))
        username_label.place(x=10, y=20)

        #-----------------------------------SideMenu Frame---------------------------------------
        SideMenuFrame = cttk.CTkFrame(root, width=200, height=450, fg_color=("white", "#4B49AC"))
        SideMenuFrame.place(x=10, y=50)

        sideMenuTitle = cttk.CTkLabel(SideMenuFrame, text=f"AVEES", font=("Arial", 24, "bold"))
        sideMenuTitle.place(x=50, y=10)

        # Dashboard
        btn_dashboard = cttk.CTkButton(SideMenuFrame, text="Dashboard", font=("Arial", 14, "bold"), height=35, width=180,
                                       command=lambda: self.show_frame(self.dashboard_frame))
        btn_dashboard.place(x=10, y=60)

        # Setting
        btn_setting = cttk.CTkButton(SideMenuFrame, text="Setting", font=("Arial", 14, "bold"), height=35, width=180,
                                     command=lambda: self.show_frame(self.settings_frame))
        btn_setting.place(x=10, y=100)

        # Components
        btn_components = cttk.CTkButton(SideMenuFrame, text="Components", font=("Arial", 14, "bold"), height=35, width=180,
                                        command=lambda: self.show_frame(self.components_frame))
        btn_components.place(x=10, y=140)

        # Logout
        btn_logout = cttk.CTkButton(SideMenuFrame, text="Logout", font=("Arial", 14, "bold"), command=self.logout,
                                    height=35, corner_radius=20)
        btn_logout.place(x=10, y=285)

    def show_frame(self, frame=None):
        if frame:
            # Hide the current frame
            self.current_frame.place_forget()

            # Update the current frame to the selected frame
            self.current_frame = frame

        # Show the selected frame
        self.current_frame.place(x=280, y=50)


    def logout(self):
        self.root.destroy()
        #  import LoginPage
        os.system("python LoginPage2.py") #better to use this
        print("logout")


# Usage example
# root = cttk.CTk()
# dashboard_obj = Dashboard(root, "Username")
# root.mainloop()
