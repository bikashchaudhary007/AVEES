import tkinter as tk

# Create a separate class for the widget
class CustomWidget(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Create the widget
        self.create_widget()

    def create_widget(self):
        # Define the widget's functionality
        self.label = tk.Label(self, text="This is a custom widget")
        self.label.pack()

# Main application class using the widget
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Widget Implementation Example")

        # Create an instance of the custom widget class
        self.custom_widget = CustomWidget(self)
        self.custom_widget.pack()

if __name__ == "__main__":
    # Create an instance of the MainApplication class
    app = MainApplication()

    # Start the application's main loop
    app.mainloop()
