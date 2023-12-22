import mysql.connector

class Model:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="aveesdb"
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

import tkinter as tk

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Tkinter MVC with MySQL")

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(padx=20, pady=20)

        self.fetch_data_button = tk.Button(self.root, text="Fetch Data", command=self.controller.fetch_data)
        self.fetch_data_button.pack(padx=10, pady=10)

    def update_result_label(self, data):
        self.result_label.config(text=str(data))


class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)

    def fetch_data(self):
        query = "SELECT * FROM vehicledetails;"
        result = self.model.execute_query(query)
        self.view.update_result_label(result)

def main():
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()

