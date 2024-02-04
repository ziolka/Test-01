from random import randrange


def get_numbers_ticket(min, max, quantity):
    print(f'{min}, {max}, {quantity}')
    if (quantity > max - min) or (min < 1) or (max > 1000):
        return []

    my_numbers = []
    
    for i in range(100):
        if len(my_numbers) >= quantity:
            break
        chosen_number = randrange(min, max)
        print(chosen_number)
        if chosen_number in my_numbers:
            print("nope") 
            continue
        else:
            my_numbers.append(chosen_number)
        
    print(my_numbers)
    my_numbers.sort()
    
    return my_numbers