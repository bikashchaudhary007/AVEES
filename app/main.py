import tkinter as tk
# from pages.login_page import LoginPage
from pages.login_page2 import LoginPage

def run_application():
    root = tk.Tk()
    login = LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    run_application()
