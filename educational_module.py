
class EducationalModule:
    def __init__(self):
        self.modules = []

    def add_module(self, module_name, description, interactive_session):
        self.modules.append((module_name, description, interactive_session))

    def list_modules(self):
        for module in self.modules:
            print(f"Module: {module[0]}, Description: {module[1]}")

    def run_module(self, module_name):
        for module in self.modules:
            if module[0] == module_name:
                module[2]()  # Execute the interactive session
                break
