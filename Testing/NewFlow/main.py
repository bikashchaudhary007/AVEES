# main.py

from app.controllers.login_controller import LoginController

if __name__ == "__main__":
    login_controller = LoginController()
    login_controller.login_view.mainloop()
