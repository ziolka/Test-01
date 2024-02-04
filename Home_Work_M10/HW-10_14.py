class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        print(self)
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contact_dict = {
            "id": Contacts.current_id,
            "name": name,
            "phone": phone,
            "email": email,
            "favorite": favorite
        }
        self.contacts.append(self.contact_dict)
        Contacts.current_id += 1
        print(f'Current ID: {self.current_id}')
        print(f'Contact dictionary: {self.contact_dict}')
        print(f'Contacts list: {self.contacts}')

        return self.contacts