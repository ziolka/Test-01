class User:
    name = "UserName"
    user_id = 1

    def say_name(self):
        print(f'Hi! I am {self.name} and my ID number is {self.user_id}')

    def set_id(self, user_id):
        self.user_id = user_id

jan = User()
jan.name = "Janek"

jan.say_name()

jan.set_id(10)
jan.say_name()

