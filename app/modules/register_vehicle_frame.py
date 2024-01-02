import tkinter as tk

class RegisterVehicle:
    def __init__(self, root):
        self.root = root

        self.register_frame = tk.Frame(self.root, width=600, height=400, bg="lightgreen")
        self.register_frame.pack_propagate(False)
        self.register_frame.pack()

        # Add widgets to the register frame
        label = tk.Label(self.register_frame, text="Register Vehicle", font=("Arial", 18))
        label.pack(pady=20)
        # Add more widgets as needed
