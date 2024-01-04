import mysql.connector

class DatabaseManager:
    def __init__(self):
        self.db_conn = None

    def connect(self):
        try:
            self.db_conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",  # Replace with your MySQL password
                database="aveesdb"
            )
            print("Connected to the database!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.db_conn = None

    def close_connection(self):
        if self.db_conn:
            self.db_conn.close()
            print("Database connection closed.")

    def execute_query(self, query, params=None):
        try:
            cursor = self.db_conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.db_conn.commit()
            return cursor
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None
        
        finally:
            if cursor:
                cursor.close()  # Close the cursor

    def fetch_one(self, cursor):
        return cursor.fetchone()

    def fetch_all(self, cursor):
        return cursor.fetchall()
