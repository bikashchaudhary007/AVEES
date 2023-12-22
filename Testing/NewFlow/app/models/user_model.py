# models/user_model.py
import mysql.connector
class User:
    def __init__(self):
        self.db_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Replace with your MySQL password
            database="aveesdb"  # Replace with your database name
        )
        # Simulating a user database (replace with actual database operations)
        self.users = {
            "user1": "password1",
            "user2": "password2",
            # Add more users if needed
        }

    def authenticate(self, username, password):
        cursor = self.db_conn.cursor()

        query = "SELECT * FROM user WHERE username = %s AND pwd = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        cursor.close()

        if user:
            return True
        return False