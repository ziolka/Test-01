def get_emails(list_contacts):
    print(list_contacts)
    for person in list_contacts:
        result = list(map(lambda person: person.get("email"), list_contacts))
        return result
    