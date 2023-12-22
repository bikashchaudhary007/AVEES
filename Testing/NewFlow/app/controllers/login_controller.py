# controllers/login_controller.py

from ..models.user_model import User
from ..views.login_view import LoginView
from ..controllers.dashboard_controller import DashboardController
from ..views.dashboard_view import DashboardView

class LoginController:
    def __init__(self):
        self.user_model = User()
        self.login_view = LoginView(self)

    def authenticate_user(self, username, password):
        return self.user_model.authenticate(username, password)
    
    def show_dashboard(self):
        self.dashboard_controller = DashboardController()
        self.dashboard_view = DashboardView(self.dashboard_controller)
        self.dashboard_view.mainloop()
        self.login_view.destroy()  # Close the login window
