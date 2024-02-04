import re

string = "The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100"

def generator_numbers(string=""):
    print(f'String from generator function: {string}')
    pattern = r'\d+'
    result = re.findall(pattern, string)
    print(f'Result: {result}')
    for item in result:
        item = int(item)
        print(f'Current item: {item}')
        yield item


def sum_profit(string):
    total_amount = 0
    print(f'String from sum profit function: {string}')
    sum = generator_numbers(string)
    for value in sum:
        total_amount = total_amount + value
        print(f'Total amount: {total_amount}')
    return(total_amount)

    
print(sum_profit(string))
