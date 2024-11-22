class PasswordManager:
    def __init__(self):
        self.__password = None  # Private attribute

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password


# Testing the class
pm = PasswordManager()
pm.set_password("secure123")
print("Password:", pm.get_password())
