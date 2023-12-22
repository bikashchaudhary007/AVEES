import tkinter as tk

class Model:
    def __init__(self):
        self.data = "Hello, Tkinter!"

    def get_data(self):
        return self.data

    def update_data(self, new_data):
        self.data = new_data

class View:
    def __init__(self, root):
        self.root = root
        self.root.title("MVC with Tkinter")

        self.label = tk.Label(self.root, text="")
        self.label.pack(padx=20, pady=20)

        self.button = tk.Button(self.root, text="Click Me")
        self.button.pack(padx=10, pady=10)

    def set_button_command(self, command):
        self.button.config(command=command)

    def update_label_text(self, new_text):
        self.label.config(text=new_text)

class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root)
        self.view.set_button_command(self.on_button_click)

    def on_button_click(self):
        new_text = "Button Clicked!"
        self.model.update_data(new_text)
        updated_data = self.model.get_data()
        self.view.update_label_text(updated_data)

def main():
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
