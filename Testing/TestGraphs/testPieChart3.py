import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkcalendar import DateEntry
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

class PieChartApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Vehicle Count Pie Chart')

        self.filter_frame = ttk.Frame(root)
        self.filter_frame.pack(padx=10, pady=10)

        self.entry_from_date = DateEntry(self.filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_from_date.grid(row=0, column=1, padx=5, pady=5)
        self.entry_from_date.set_date(datetime.now().replace(day=1))  # Default start date (1st day of current month)

        self.entry_to_date = DateEntry(self.filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_to_date.grid(row=0, column=3, padx=5, pady=5)
        self.entry_to_date.set_date(datetime.now())  # Default end date (current date)

        self.label_from_date = ttk.Label(self.filter_frame, text='From Date:')
        self.label_from_date.grid(row=0, column=0, padx=5, pady=5)

        self.label_to_date = ttk.Label(self.filter_frame, text='To Date:')
        self.label_to_date.grid(row=0, column=2, padx=5, pady=5)

        self.graph_frame = ttk.Frame(root)
        self.graph_frame.pack()

        self.entry_from_date.bind("<<DateEntrySelected>>", self.update_pie_chart)
        self.entry_to_date.bind("<<DateEntrySelected>>", self.update_pie_chart)

        # Initially, show pie chart for the current month
        self.update_pie_chart(None)

    def fetch_data_from_db(self, from_date, to_date):
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Enter your MySQL password here
            database='aveesdb'
        )

        cursor = connection.cursor()

        query = "SELECT DATE_FORMAT(Entry_Time, '%Y-%m-%d') AS Entry_Date, COUNT(*) AS Vehicle_Count FROM vehicledetails WHERE Entry_Time BETWEEN %s AND %s GROUP BY Entry_Date"
        cursor.execute(query, (from_date, to_date))

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        return rows

    def update_pie_chart(self, event):
        from_date = self.entry_from_date.get_date().strftime('%Y-%m-%d')  # Selected 'from' date
        to_date = self.entry_to_date.get_date().strftime('%Y-%m-%d')  # Selected 'to' date

        rows = self.fetch_data_from_db(from_date, to_date)

        x_data = [row[0] for row in rows]
        y_data = [row[1] for row in rows]

        labels = x_data
        sizes = y_data

        # Clear previous plot
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')

        ax.set_title('Vehicle Distribution Based on Dates')

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

def main():
    root = tk.Tk()
    app = PieChartApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
