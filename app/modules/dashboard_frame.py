import tkinter as tk

class DashboardMainFrame:
    def __init__(self, root):
        self.root = root

        self.dashboard_frame = tk.Frame(self.root, width=600, height=400, bg="lightblue")
        self.dashboard_frame.pack_propagate(False)
        self.dashboard_frame.pack()

        # Add widgets to the dashboard frame
        label = tk.Label(self.dashboard_frame, text="Dashboard Main Frame", font=("Arial", 18))
        label.pack(pady=20)
        # Add more widgets as needed
