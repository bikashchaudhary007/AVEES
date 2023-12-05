import customtkinter as cttk

class ToplevelWindow(cttk.CTkToplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("TopLevel")
        self.geometry("500x500+50+0")
        self.resizable(False, False)

# Usage example
root = cttk.CTk()
toplevel_window = ToplevelWindow(root)
# root.mainloop()
