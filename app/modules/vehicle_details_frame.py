import tkinter as tk

class VehicleDetails:
    def __init__(self, root):
        self.root = root

        self.details_frame = tk.Frame(self.root, width=600, height=400, bg="lightyellow")
        self.details_frame.pack_propagate(False)
        self.details_frame.pack()

        # Add widgets to the vehicle details frame
        label = tk.Label(self.details_frame, text="Vehicle Details", font=("Arial", 18))
        label.pack(pady=20)
        # Add more widgets as needed
