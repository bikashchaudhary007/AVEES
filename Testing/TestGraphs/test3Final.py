import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar
from datetime import datetime, date  # Import datetime module and date class

def get_current_month_dates():
    today = date.today()
    first_day = today.replace(day=1)
    last_day = today.replace(day=28)
    last_day = last_day.replace(day=max(min(31, last_day.day), 29))
    return first_day, last_day

def plot_vehicle_count(from_date, to_date):
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

    for widget in graph_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(x_data, y_data, color='skyblue')

    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Number of Vehicles', fontsize=12)
    ax.set_title('Number of Vehicles Entered on Different Days', fontsize=14)
    ax.set_xticklabels(x_data, rotation=0)

    ax.set_facecolor('lightgray')

    for bar, count in zip(bars, y_data):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), count,
                ha='center', va='bottom', color='black', fontsize=10)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    print("From Date:", from_date_formatted)
    print("To Date:", to_date_formatted)
    print("Query Executed Successfully")
    print("Rows Fetched:", rows)

root = tk.Tk()
root.title('Vehicle Count by Date in Tkinter')

style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack()

filter_frame = ttk.Frame(main_frame)
filter_frame.pack()

current_month_start, current_month_end = get_current_month_dates()

entry_from_date = DateEntry(filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_from_date.grid(row=0, column=1, padx=5, pady=5)
entry_from_date.set_date(current_month_start.strftime('%m/%d/%y'))

entry_to_date = DateEntry(filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_to_date.grid(row=0, column=3, padx=5, pady=5)
entry_to_date.set_date(current_month_end.strftime('%m/%d/%y'))

label_from_date = ttk.Label(filter_frame, text='From Date:')
label_from_date.grid(row=0, column=0, padx=5, pady=5)

label_to_date = ttk.Label(filter_frame, text='To Date:')
label_to_date.grid(row=0, column=2, padx=5, pady=5)

graph_frame = ttk.Frame(main_frame)
graph_frame.pack()

plot_vehicle_count(current_month_start, current_month_end)

def update_graph(event):
    from_date = datetime.strptime(entry_from_date.get(), '%m/%d/%y')
    to_date = datetime.strptime(entry_to_date.get(), '%m/%d/%y')
    plot_vehicle_count(from_date, to_date)

entry_from_date.bind("<<DateEntrySelected>>", update_graph)
entry_to_date.bind("<<DateEntrySelected>>", update_graph)

root.mainloop()
