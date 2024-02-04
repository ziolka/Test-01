class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Owner:
    def __init__(self, name, age, adress):
        self.name = name
        self.age = age
        self.adress = adress

    def info(self):
        return {"name": self.name, "age":self.age, "adress": self.adress}
            
        
        


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        print(self.owner.info())
        return self.owner.info()