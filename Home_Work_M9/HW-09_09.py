def positive_values(list_payment):
    result = list(filter(lambda amount: amount > 0, list_payment))
    return result