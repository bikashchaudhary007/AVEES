# controllers/dashboard_controller.py

from ..models.vehicle_model import Vehicle  # Assuming you have a Vehicle model

class DashboardController:
    def __init__(self):
        self.vehicle_model = Vehicle()  # Initialize the Vehicle model

    def fetch_total_vehicles(self):
        # Method to retrieve the total number of vehicles (Example logic)
        return self.vehicle_model.get_total_vehicles()  # Implement this in Vehicle model

    def fetch_recent_entries(self):
        # Method to fetch recent vehicle entries (Example logic)
        return self.vehicle_model.get_recent_entries()  # Implement this in Vehicle model

    # Add more methods as per your dashboard functionalities
