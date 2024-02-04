class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        return f"Hi {self.name}"
    
p = Person("Boris", 44)
print(p.name)
print(p.age)
print(p.greetings())