def get_favorites(contacts):
    print(contacts)
    for person in contacts:
        result = list(filter(lambda person: person["favorite"] == True, contacts))
        return result
