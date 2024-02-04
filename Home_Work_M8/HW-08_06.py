from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    print(number_list)
    print(signs_count)

    if len(number_list) == 0:
        return None
    sum = Decimal(0) 
    getcontext().prec = 6
    for i in range(len(number_list)):
        sum  = Decimal(sum) + Decimal(number_list[i])
        print(f' Sum: {sum}')
        average = Decimal(sum / len(number_list))

        print(f' Average: {average}')

    return average
