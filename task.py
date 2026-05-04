class User:
    count = 0
    def __init__(self:str, name:str, login:str, password:str, grade:int):
        self.name = name
        self._login = login
        self._password = password
        self._grade = grade
        User.count += 1

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        print("You cant change login")

    @property
    def password(self):
        return "*********"

    @password.setter
    def password(self, value):
        self._password = value



    def show_info(self):
        print(f"Name: {self.name}, login: {self._login}" )

    @property
    def grade(self):
        return "Unknown property grade"

    @grade.setter
    def grade(self,value):
        print("Unknown property grade")

    def __lt__(self,other):
        return self._grade < other._grade

    def __gt__(self,other):
        return self._grade > other._grade

    def __eq__(self,other):
        return self._grade == other._grade




class SuperUser(User):
    count = 0
    def __init__(self:str, name:str, login:str, password:str,
role:str, grade:int):
        self.name = name
        self._login = login
        self._password = password
        self._role = role
        self._grade = grade
        SuperUser.count += 1

    def show_info(self):
        print(f"Name: {self.name}, login: {self._login}, role: {self._role}" )


user1 = User('dsf', 'fd', '1234f', 3)
user2 = User('aaaaaa', 'asdf', 'dsf', 2)
user3 = User('mihail', 'miha', 'kurica', 2)
user4 = SuperUser('llllll', 'llls', 'sdsdsdsd', 'admin', 1)

print('-------')
user1.show_info()
print('-------')

print(user1.password)
print(user1.login)
print('-------')
user1.password = 213
user1.name = "dsff"
print(user1.name)
user1.login = 'geo'
print('-------')
user1.grade = 1
print(user1.grade)
print('-------')
print(user1 < user2)
print(user2 == user3)
print(user4 > user1)
print('-------')
print(f'users: {User.count}')
print(f'superusers:  {SuperUser.count}')