from collections import UserString


class NumberString(UserString):
    def number_count(self):
        print(f'Self: {self}')
        digit_number = 0
        for sign in self.data:
            if sign.isdigit():
                digit_number += 1
            
        return digit_number