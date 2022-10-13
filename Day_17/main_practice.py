class User:
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name

# To name the first letter of name should be caps "PascalCase"

user_1 = User("001", "Venky")
user_2 = User("002", "krishna")
print(user_1.id)

