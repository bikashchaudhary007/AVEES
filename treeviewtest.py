import tkinter as tk
from tkinter import ttk

def create_treeview():
    tree = ttk.Treeview(root, columns=('Name', 'Age', 'Country'), show='headings')

    # Define column headings
    tree.heading('Name', text='Name')
    tree.heading('Age', text='Age')
    tree.heading('Country', text='Country')

    # Add data to the treeview
    data = [('John Doe', 25, 'USA'),
            ('Jane Smith', 30, 'Canada'),
            ('Bob Johnson', 22, 'UK')]

    for item in data:
        tree.insert('', 'end', values=item)

    # Style the treeview
    style = ttk.Style()
    style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))
    style.configure("Treeview", font=('Helvetica', 10))

    tree.grid(row=0, column=0, padx=10, pady=10)

root = tk.Tk()
root.title("Styled Treeview Example")

create_treeview()

root.mainloop()
