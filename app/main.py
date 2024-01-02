import tkinter as tk
from pages.login_page import LoginPage

def run_application():
    root = tk.Tk()
    login = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    run_application()
