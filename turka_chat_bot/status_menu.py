import json_manager
class status_menu:
    def __init__(self, menu):
        self.menu = json_manager.get_menu()

    def save_status(self, menu):
        self.menu = menu

    def get_menu(self):
        return self.menu