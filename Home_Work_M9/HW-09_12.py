payment = [100, -3, 400, 35, -100]

from functools import reduce


def amount_payment(payment):

    return reduce((lambda x, y: x + y if (y > 0) else x), payment)

print(amount_payment(payment))