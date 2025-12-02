class User:

    def __init__(self, user_id: int, username: str): # Object
        print("new user being created!")

        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): # Method
        user.followers += 1
        self.following += 1




user_1 = User(1, "Angela")
user_2 = User(2, "Jack")

user_1.follow(user_2)

print(f"User: {user_1.id}, is: {user_1.username}, has: {user_1.followers} followers, following: {user_1.following}")
print(f"User: {user_2.id}, is: {user_2.username}, has: {user_2.followers} followers, following: {user_2.following}")
