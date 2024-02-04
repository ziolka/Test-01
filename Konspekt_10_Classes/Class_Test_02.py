class Human:
    name = ""

    def hello(self, val):
        if self.name:
            return f'Hello {val}! I am {self.name}.'
        return f'Hello {val}!'
    
bill = Human()
print(bill.hello("John"))

bill.name = "Billy"
print(bill.hello("John"))