import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def plot_bar_graph():
    categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
    values = [25, 40, 30, 35, 20]

    fig, ax = plt.subplots()
    bars = ax.bar(categories, values, color='skyblue')

    # Modify plot parameters as needed
    ax.set_xlabel('Categories', fontsize=12)
    ax.set_ylabel('Values', fontsize=12)
    ax.set_title('Bar Graph', fontsize=14)

    # Add gridlines
    ax.grid(True, axis='y', linestyle='--', alpha=0.7)

    # Set background color of the plot
    ax.set_facecolor('lightgray')

    # Add data labels on top of each bar
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval + 0.2, round(yval, 2), ha='center', va='bottom')

    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root = tk.Tk()
root.title('Bar Graph in Tkinter')

style = ttk.Style()
style.configure('TButton', font=('Arial', 12))

main_frame = ttk.Frame(root, padding=20)
main_frame.pack()

graph_frame = ttk.Frame(main_frame)
graph_frame.pack()

plot_button = ttk.Button(main_frame, text='Plot Bar Graph', command=plot_bar_graph)
plot_button.pack()

root.mainloop()
