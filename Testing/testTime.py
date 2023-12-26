import tkinter as tk
from datetime import datetime

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock")
        
        self.label = tk.Label(root, font=('Arial', 24), fg='black')
        self.label.pack(padx=20, pady=20)
        
        self.update_time()
    
    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.label.config(text=current_time)
        self.label.after(1000, self.update_time)  # Update time every 1000 milliseconds (1 second)

def main():
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
