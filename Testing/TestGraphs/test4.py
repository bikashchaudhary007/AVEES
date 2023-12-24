import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
from tkcalendar import DateEntry
from datetime import datetime, date

import customtkinter as cttk

class VehicleCountApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Vehicle Count by Date in Tkinter')

        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12))


        self.filter_frame = ttk.Frame(root)
        self.filter_frame.place(x=10,y=10)

        self.current_month_start, self.current_month_end = self.get_current_month_dates()

        self.entry_from_date = DateEntry(self.filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_from_date.grid(row=0, column=1, padx=5, pady=5)
        self.entry_from_date.set_date(self.current_month_start.strftime('%m/%d/%y'))

        self.entry_to_date = DateEntry(self.filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.entry_to_date.grid(row=0, column=3, padx=5, pady=5)
        self.entry_to_date.set_date(self.current_month_end.strftime('%m/%d/%y'))

        self.label_from_date = ttk.Label(self.filter_frame, text='From Date:')
        self.label_from_date.grid(row=0, column=0, padx=5, pady=5)

        self.label_to_date = ttk.Label(self.filter_frame, text='To Date:')
        self.label_to_date.grid(row=0, column=2, padx=5, pady=5)

        self.graph_frame = ttk.Frame(root, width=650, height=650)
        self.graph_frame.place(x=50,y=150)

        self.plot_vehicle_count(self.current_month_start, self.current_month_end)

        self.entry_from_date.bind("<<DateEntrySelected>>", self.update_graph)
        self.entry_to_date.bind("<<DateEntrySelected>>", self.update_graph)

    def get_current_month_dates(self):
        today = date.today()
        first_day = today.replace(day=1)
        last_day = today.replace(day=28)
        last_day = last_day.replace(day=max(min(31, last_day.day), 29))
        return first_day, last_day

    def plot_vehicle_count(self, from_date, to_date):
        from_date_str = from_date.strftime('%m/%d/%y')
        to_date_str = to_date.strftime('%m/%d/%y')

        from_date_formatted = from_date.strftime('%Y-%m-%d')
        to_date_formatted = to_date.strftime('%Y-%m-%d')

        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='aveesdb'
        )

        cursor = connection.cursor()

        query = "SELECT DATE_FORMAT(Entry_Time, '%Y-%m-%d') AS Entry_Date, COUNT(*) AS Vehicle_Count FROM vehicledetails WHERE Entry_Time BETWEEN %s AND %s GROUP BY Entry_Date"
        cursor.execute(query, (from_date_formatted, to_date_formatted))

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        x_data = [row[0] for row in rows]
        y_data = [row[1] for row in rows]

        # Clear previous plot data
        for widget in self.graph_frame.winfo_children():
            widget.destroy()

        fig, ax = plt.subplots(figsize=(4, 5))
        bars = ax.bar(x_data, y_data, color='skyblue')

        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Number of Vehicles', fontsize=12)
        ax.set_title('Number of Vehicles Entered on Different Days', fontsize=14)
        ax.set_xticklabels(x_data, rotation=45)

        ax.set_facecolor('lightgray')

        for bar, count in zip(bars, y_data):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), count,
                    ha='center', va='bottom', color='black', fontsize=10)

        canvas = FigureCanvasTkAgg(fig, master=self.graph_frame)
        canvas.draw()
        canvas.get_tk_widget().place(x=100,y=100)

        print("From Date:", from_date_formatted)
        print("To Date:", to_date_formatted)
        print("Query Executed Successfully")
        print("Rows Fetched:", rows)

    def update_graph(self, event):
        from_date = datetime.strptime(self.entry_from_date.get(), '%m/%d/%y')
        to_date = datetime.strptime(self.entry_to_date.get(), '%m/%d/%y')
        self.plot_vehicle_count(from_date, to_date)

def main():
    # root = tk.Tk()
    root = cttk.CTk()
    app = VehicleCountApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
