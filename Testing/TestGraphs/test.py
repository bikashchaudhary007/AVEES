import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar
from datetime import datetime  # Import datetime module

def plot_vehicle_count():
    from_date_str = entry_from_date.get()
    to_date_str = entry_to_date.get()

    # Convert strings to datetime objects
    from_date = datetime.strptime(from_date_str, '%m/%d/%y')  # Updated format string
    to_date = datetime.strptime(to_date_str, '%m/%d/%y')  # Updated format string

    # Format datetime objects to the desired format
    from_date_formatted = from_date.strftime('%Y-%m-%d')
    to_date_formatted = to_date.strftime('%Y-%m-%d')

    # Connect to MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Enter your password if required
        database='aveesdb'
    )

    cursor = connection.cursor()

    # Query to fetch vehicle count for each day within the selected date range
    query = "SELECT DATE_FORMAT(Entry_Time, '%Y-%m-%d') AS Entry_Date, COUNT(*) AS Vehicle_Count FROM vehicledetails WHERE Entry_Time BETWEEN %s AND %s GROUP BY Entry_Date"
    cursor.execute(query, (from_date_formatted, to_date_formatted))  # Use formatted dates

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    connection.close()

    # Extract x (dates) and y (vehicle counts) data from the rows
    x_data = [row[0] for row in rows]  # Dates already formatted as strings
    y_data = [row[1] for row in rows]

    # Clear the previous plot
    for widget in graph_frame.winfo_children():
        widget.destroy()

    # Plotting the data with adjusted figure size
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(x_data, y_data, color='skyblue')

    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Number of Vehicles', fontsize=12)
    ax.set_title('Number of Vehicles Entered on Different Days', fontsize=14)
    ax.set_xticklabels(x_data, rotation=0)  # Rotate x-axis labels for better readability

    ax.set_facecolor('lightgray')

    for bar, count in zip(bars, y_data):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), count,
                ha='center', va='bottom', color='black', fontsize=10)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    # Inside plot_vehicle_count()
    print("From Date:", from_date_formatted)
    print("To Date:", to_date_formatted)
    print("Query Executed Successfully")

    # After fetching rows
    print("Rows Fetched:", rows)

def update_graph(event):
    plot_vehicle_count()

# Create the GUI window
root = tk.Tk()
root.title('Vehicle Count by Date in Tkinter')

style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack()

filter_frame = ttk.Frame(main_frame)
filter_frame.pack()

entry_from_date = DateEntry(filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_from_date.grid(row=0, column=1, padx=5, pady=5)

entry_to_date = DateEntry(filter_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_to_date.grid(row=0, column=3, padx=5, pady=5)

label_from_date = ttk.Label(filter_frame, text='From Date:')
label_from_date.grid(row=0, column=0, padx=5, pady=5)

label_to_date = ttk.Label(filter_frame, text='To Date:')
label_to_date.grid(row=0, column=2, padx=5, pady=5)

plot_button = ttk.Button(filter_frame, text='Plot Graph', command=plot_vehicle_count)
plot_button.grid(row=0, column=4, padx=5, pady=5)

graph_frame = ttk.Frame(main_frame)
graph_frame.pack()

entry_from_date.bind("<<DateEntrySelected>>", update_graph)
entry_to_date.bind("<<DateEntrySelected>>", update_graph)

root.mainloop()
