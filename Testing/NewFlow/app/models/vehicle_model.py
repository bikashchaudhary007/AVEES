# models/vehicle_model.py

import mysql.connector  # Import the MySQL connector

class Vehicle:
    def __init__(self):
        # Initialize database connection
        self.db_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="aveesdb"  # Replace with your database name
        )

    def get_total_vehicles(self):
        # Fetch the total number of vehicles from the database
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM vehicledetails")
            total_vehicles = cursor.fetchone()[0]
            cursor.close()
            return total_vehicles
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return 0  # Return 0 in case of an error

    def get_recent_entries(self):
        # Fetch recent vehicle entries from the database
        try:
            cursor = self.db_conn.cursor()
            cursor.execute("SELECT * FROM vehicledetails ORDER BY Entry_Time DESC LIMIT 10")
            recent_entries = cursor.fetchall()
            cursor.close()
            return recent_entries
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []  # Return an empty list in case of an error

    # Implement other methods for CRUD operations (insert, update, delete) as needed
