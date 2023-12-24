# controllers/dashboard_controller.py
import os
from ..models.vehicle_model import Vehicle  # Assuming you have a Vehicle model
from ..views.dashboard_view import DashboardView

class DashboardController:
    def __init__(self):
        self.vehicle_model = Vehicle()  # Initialize the Vehicle model
        self.dashboard_view = DashboardView(self)

    
    def logout(self):
       # Perform logout actions here if needed (clear session, etc.)
        print("Logging out...")  # Placeholder for logout actions

    def fetch_total_vehicles(self):
        # Method to retrieve the total number of vehicles (Example logic)
        return self.vehicle_model.get_total_vehicles()  # Implement this in Vehicle model

    def fetch_recent_entries(self):
        # Method to fetch recent vehicle entries (Example logic)
        return self.vehicle_model.get_recent_entries()  # Implement this in Vehicle model

    # Add more methods as per your dashboard functionalities
