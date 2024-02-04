class MyList:
    def __init__(self):
        self.elements = []

    def __getitem__(self, index):
        return self.elements[index]
    
    def __setitem__(self, index, value):
        self.elements[index] = value

    def append(self, value):
        self.elements.append(value)

    def __len__(self):
        return len(self.elements)
    
my_list = MyList()
my_list.append(10)
my_list.append(20)
my_list.append(30)

print(my_list[0])
print(my_list[1])
my_list[1] = 25
print(my_list[1])
print(len(my_list))