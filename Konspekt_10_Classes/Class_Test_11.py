import string

class NameToShortError(Exception):
    pass

class NameStartsFromLowError(Exception):
    pass

def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameToShortError
    if name[0] not in string.ascii_uppercase:
        raise NameStartsFromLowError
        
while True:
    try:
        name = enter_name()
        break
    except NameToShortError:
        print("Name ist to short. At least 3 symbols are required. Try again.")
    except NameStartsFromLowError:
        print("Name shuld start from capital letter. Try again.")