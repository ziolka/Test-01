class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
       
    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, color):
        Animal.color = "red"

first_animal = Animal("Doggy", 10)
second_animal = Animal("Catty", 5)

print(first_animal.color)
first_animal.change_color("red")
print(first_animal.color)