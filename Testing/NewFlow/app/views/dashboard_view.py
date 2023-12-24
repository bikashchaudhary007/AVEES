# views/dashboard_view.py

# import tkinter as tk
import customtkinter as cttk
class DashboardView(cttk.CTk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Dashboard")
        self.geometry("1280x750+50+0")
        # self.resizable(False, False)

        # Implement dashboard UI elements
        
        # Create frames for dashboard, settings, and components
        self.dashboard_frame = cttk.CTkFrame(self, width=850, height=450, fg_color=("white", "#4B49AC"))
        self.settings_frame = cttk.CTkFrame(self, width=850, height=450, fg_color=("white", "#4B49AC"))
        self.components_frame = cttk.CTkFrame(self, width=850, height=450, fg_color=("white", "#4B49AC"))

        # Initial frame to show is the dashboard frame
        self.current_frame = self.dashboard_frame
        self.show_frame()

        
        # Displaying the username on the dashboard
        username_label = cttk.CTkLabel(self.dashboard_frame, text=f"Welcome, Admin!", font=("Arial", 16, "bold"))
        username_label.place(x=10, y=20)

        #-----------------------------------SideMenu Frame---------------------------------------
        SideMenuFrame = cttk.CTkFrame(self, width=200, height=450, fg_color=("white", "#4B49AC"))
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

        # Register Vehicle
        btn_components = cttk.CTkButton(SideMenuFrame, text="Register", font=("Arial", 14, "bold"), height=35, width=180)
        btn_components.place(x=10, y=180)

        # Logout
        btn_logout = cttk.CTkButton(SideMenuFrame, text="Logout", font=("Arial", 14, "bold"),command=self.perform_logout,
                                    height=35, corner_radius=20)
        btn_logout.place(x=10, y=285)

    def show_frame(self, frame=None):
        if frame:
            # # Stop RFID scanning when switching to the settings frame
            # if frame == self.settings_frame:
            #     self.stop_rfid_scan_thread()

            # if frame == self.dashboard_frame:
            #     self.rfid_scan_background() 

            # Hide the current frame
            self.current_frame.place_forget()

            # Update the current frame to the selected frame
            self.current_frame = frame

            

        # Show the selected frame
        self.current_frame.place(x=280, y=50)
        # Update the total number of vehicles when switching to the dashboard frame
        if frame == self.dashboard_frame:
            self.update_total_vehicles_label()

            # Refresh the treeview to apply the font changes
            self.treeview.update_idletasks()

    # def perform_logout(self):
    #     self.controller.logout()  # Call logout method in DashboardController
    #     self.destroy()  # Destroy the current dashboard view

    #     # Open the login view (assuming it's in the main module)
    #     import main  # Import the main module where the login view is instantiated
    #     main.show_login_view()  # Call a function in main.py to display the login view

    def perform_logout(self):
        self.controller.logout()  # Call logout method in DashboardController
        self.destroy_login_view()  # Destroy the login view window and return to the login interface

    def destroy_login_view(self):
        # Destroy the login view window created by main.py
        self.master.destroy()  # This assumes the login view is the root window created by main.py
        

