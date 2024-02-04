def formatted_numbers():
    result = ["| decimal  |   hex    |  binary  |"]  

    for num in range(16):
        el = "|{:<10}|{:^10}|{:>10}|".format(num, hex(num)[2:], bin(num)[2:])
        print(el)
        # new_el = (
        #     el.replace("0b", "  ")
        #     .replace("0x", "  ")
        #             )
        result.append(el)
        # joined_result = "\n".join(result)
        
    print(result)
    return result

# [2:] użyj slicingu do wzięcia całej liczby hex np. oprócz dwóch pierwszych znaków
