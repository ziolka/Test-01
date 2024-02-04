from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        print(self.data)
        sum = 0
        for value in self.data:
            if value > 0:
                sum = sum + value
        print(f'Sum: {sum}')
        return sum