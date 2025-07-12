class User:
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user = object):
        user.followers += 1
        self.following += 1

user_1 = User("001", "Angela")
user_2 = User("002", "Jack")

user_1.follow(user_2)