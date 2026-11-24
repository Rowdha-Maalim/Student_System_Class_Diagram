class User:
    def __init__(self, user_id, name, email, password):
        if not user_id or not name or not email or not password:
            raise ValueError("User information cannot be empty.")
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        
    def login(self):
        return True
    def logout(self):
        print(f"{self.name} has logged out.")