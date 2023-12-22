import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar

def choose_date(entry):
    date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):")
    if date:
        entry.delete(0, tk.END)
        entry.insert(0, date)

def plot_vehicle_count():
    from_date = entry_from_date.get()
    to_date = entry_to_date.get()

    # Connect to MySQL database
    # Connect to MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='aveesdb'
    )

    cursor = connection.cursor()

    # Query to fetch vehicle count for each day
    cursor.execute("SELECT DATE(Entry_Time) AS Entry_Date, COUNT(*) AS Vehicle_Count FROM vehicledetails GROUP BY Entry_Date")

    # Fetch all rows from the result
    rows = cursor.fetchall()

    # Extract x (dates) and y (vehicle counts) data from the rows
    x_data = [row[0].strftime('%Y-%m-%d') for row in rows]  # Convert date to string format
    y_data = [row[1] for row in rows]

    # Close cursor and connection
    cursor.close()
    connection.close()

    # Plotting the data with adjusted figure size
    fig, ax = plt.subplots(figsize=(8, 6))  # Increase figure size here (width, height)
    bars = ax.bar(x_data, y_data, color='skyblue')

    # Modify plot parameters as needed
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Number of Vehicles', fontsize=12)
    ax.set_title('Number of Vehicles Entered on Different Days', fontsize=14)
    ax.set_xticklabels(x_data, rotation=0)  # Rotate x-axis labels for better readability

    # Set background color of the plot
    ax.set_facecolor('lightgray')

    # Annotate each bar with the count at the top
    for bar, count in zip(bars, y_data):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), count,
                ha='center', va='bottom', color='black', fontsize=10)

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root = tk.Tk()
root.title('Vehicle Count by Date in Tkinter')

style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack()

filter_frame = ttk.Frame(main_frame)
filter_frame.pack()

# Replace Entry widgets with DateEntry widgets
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

root.mainloop()
