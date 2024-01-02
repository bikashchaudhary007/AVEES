import tkinter as tk
from modules.dashboard_frame import DashboardMainFrame
from modules.register_vehicle_frame import RegisterVehicle
from modules.vehicle_details_frame import VehicleDetails

class DashboardPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")

        # # Create instances of different modules/components
        # self.dashboard_main_frame = DashboardMainFrame(self.root)
        # self.register_vehicle = RegisterVehicle(self.root)
        # self.vehicle_details = VehicleDetails(self.root)


        # Create the side menu
        self.side_menu_frame = tk.Frame(self.root, width=200, bg="lightgray")
        self.side_menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Add buttons/options in the side menu to open modules
        self.dashboard_button = tk.Button(self.side_menu_frame, text="Dashboard Main Frame", command=self.show_dashboard_main_frame)
        self.dashboard_button.pack(fill=tk.X, padx=10, pady=5)

        self.register_button = tk.Button(self.side_menu_frame, text="Register Vehicle", command=self.show_register_vehicle)
        self.register_button.pack(fill=tk.X, padx=10, pady=5)

        self.details_button = tk.Button(self.side_menu_frame, text="Vehicle Details", command=self.show_vehicle_details)
        self.details_button.pack(fill=tk.X, padx=10, pady=5)

        # Create frames for modules
        self.dashboard_frame = tk.Frame(self.root, width=600, height=400, bg="white")
        self.register_frame = tk.Frame(self.root, width=600, height=400, bg="white")
        self.details_frame = tk.Frame(self.root, width=600, height=400, bg="white")

        # Add labels to each module
        self.dashboard_label = tk.Label(self.dashboard_frame, text="Dashboard Main Frame", font=("Arial", 18))
        self.dashboard_label.pack(pady=20)

        self.register_label = tk.Label(self.register_frame, text="Register Vehicle", font=("Arial", 18))
        self.register_label.pack(pady=20)

        self.details_label = tk.Label(self.details_frame, text="Vehicle Details", font=("Arial", 18))
        self.details_label.pack(pady=20)


        # Pack only the dashboard frame initially
        self.dashboard_frame.pack_propagate(False)
        self.dashboard_frame.pack()

    def show_dashboard_main_frame(self):
        # Hide other frames and show Dashboard Main Frame
        self.register_frame.pack_forget()
        self.details_frame.pack_forget()
        self.dashboard_frame.pack()

        # Update or populate Dashboard Main Frame widgets
        # Add widgets and logic specific to Dashboard Main Frame

    def show_register_vehicle(self):
        # Hide other frames and show Register Vehicle
        self.dashboard_frame.pack_forget()
        self.details_frame.pack_forget()
        self.register_frame.pack()

        # Update or populate Register Vehicle widgets
        # Add widgets and logic specific to Register Vehicle

    def show_vehicle_details(self):
        # Hide other frames and show Vehicle Details
        self.dashboard_frame.pack_forget()
        self.register_frame.pack_forget()
        self.details_frame.pack()

        # Update or populate Vehicle Details widgets
        # Add widgets and logic specific to Vehicle Details