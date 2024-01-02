# # main.py

import customtkinter as cttk

from app.controllers.login_controller import LoginController

if __name__ == "__main__":
    login_controller = LoginController()
    login_controller.login_view.mainloop()


# from app.controllers.login_controller import LoginController

# if __name__ == "__main__":
#     root = cttk.CTk()  # Create the root window for the login view
#     login_controller = LoginController()  # Pass the root window to the LoginController
#     root.mainloop()
