class User:

    def __init__(self,username,password,age,career):
        self.username = username
        self.password = password
        self.age = age
        self.career = career

    def showUser(self):
        print("Username : ",self.username,"Password : ",self.password)

    def getUserName(self):
        return self.username
    def getPassword(self):
        return self.password