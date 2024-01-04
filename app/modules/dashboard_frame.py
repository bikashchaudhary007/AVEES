import tkinter as tk

class DashboardMainFrame:
    def __init__(self, root):
        self.root = root

        self.dashboard_frame = tk.Frame(self.root, width=600, height=400, bg="lightblue")
        self.dashboard_frame.pack()

        label = tk.Label(self.dashboard_frame, text="Dashboard Main Frame", font=("Arial", 18))
        label.pack(pady=20)

        title = tk.Label(self.dashboard_frame, text="Title", font=("Arial", 14), fg="black")
        title.pack(pady=20)

# Testing the DashboardMainFrame independently
if __name__ == "__main__":
    root = tk.Tk()
    dashboard = DashboardMainFrame(root)
    root.mainloop()
