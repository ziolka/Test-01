class PositiveNumber:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if new_value > 0:
            self.__value = new_value
        else:
            print('Only numbers greater zero accepted')

p = PositiveNumber()
p.value = 1
print(p.value)# 1
p.value = -1# Only numbers greater zero accepted
p._PositiveNumber__value = -1
print(p.value)# -1s