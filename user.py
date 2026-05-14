class User:
    def __init__ (self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.expenses = []

    def to_dict(self):
        return {
            "name": self.name,
            "username": self.username,
            "password": self.password,
            "expenses": self.expenses
        }

    @staticmethod
    def from_dict(data):
        user =  User(
            data["name"],
            data["username"],
            data["password"]
        )
        user.expenses = data["expenses"]
        return user