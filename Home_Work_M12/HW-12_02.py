import json


def write_contacts_to_file(filename, contacts):
    contacts = {'contacts': contacts}
    with open(filename, "w") as fh:
        json.dump(contacts, fh)

def read_contacts_from_file(filename):
    with open(filename, "r") as fh:
        unpacked = json.load(fh)
        print(unpacked)
        return unpacked.get("contacts")
    
