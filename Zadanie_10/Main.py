""""Home Work 10 - Personal Asistant with Classes"""

from collections import UserDict


class Field:
    """This is intenionally blank class for future use"""
    pass
     
class Name(Field):
    """Contains required Name field"""
    def __init__(self, name):
        self.name = name

class Phone(Field):
    """Contains optional Phone field"""
    def __init__(self, number):
        self.number = number

class Record:
    """Logic and fields management"""
    def __init__(self, name:str):
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
        else:
            print(f'The phone number {phone} has not been found for remove.')

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            index = self.phones.index(old_phone)
            self.phones[index] = new_phone
        else:
            print(f'The phone number {old_phone} has not been found for change.')

class AddressBook(UserDict):
    """Logic for record searching and management"""
    def add_record(self, record):
        self.data[record.name] = record

    def remove_record (self, name):
        if name in self.data:
            del self.data[name]
            print(f'Record with name {name} has been removed')
        else:
            print(f'Record with name {name} has not been found for remove.')

    def find_contact(self, pattern):
        results = []
        for name, record in self.data.items():
            if pattern.lower() in name.lower():
                results.append(record)
                return results
        else:
            print(f'Contact with name {name} has not been found.')


class AddressBookInterface:
    def __init__(self):
        self.address_book = AddressBook()

    def cli_add_contact(self, entry):
        name = input("Enter name: ")
        record = Record(name)
        phone = input("Enter phone number (optional)): ")
        if phone:
            record.add_phone(phone)
        self.address_book.add_record(record)
        print("Contact has been added.")

    def cli_find_contact(self, entry):
        """Find contacts"""
        pattern = input("Enter pattern to be found: ")
        results = self.address_book.search_records(pattern)
        if results:
            print("Following contacts fulfill given pattern:")
            for record in results:
                print(f"Name: {record.name}")
                if record.phones:
                    for phone in record.phones:
                        print(f"Phone number: {phone}")
                else:
                    print("No phone number.")
        else:
            print("No contacts with given searching pattern.")

    def cli_show_all(self, entry):
        """Show complete adress book"""
        for record in self.address_book.data:
            print(f"Name: {record}")    
    
    def cli_del_contact(self, entry):
        """Delete contact"""
        name = input("Enter name of the contact to be deleted: ")
        self.address_book.remove_record(name)
        print(f"Contact {name} has been deleted.")

    def cli_edit_phone(self, entry):
        """Edit phone number for given contact"""
        name = input("Enter contact name: ")
        if name in self.address_book.data:
            record = self.address_book.data[name]
            old_phone = input("Enter old phone number: ")
            new_phone = input("Enter new phone number: ")
            record.edit_phone(old_phone, new_phone)
            print("Phone number has been updated.")
        else:
            print(f"Contact with {name} does not exists.")

    def cli_del_phone(self, entry):
        """Delete phone number for given contact"""
        name = input("Enter contact name: ")
        if name in self.address_book.data:
            record = self.address_book.data[name]
            phone = input("Enter phone number to delete: ")
            record.remove_phone(phone)
            print("Phone number has been deleted.")
        else:
            print(f"Contact with name {name} does not exists.")

    def cli_exit(self):
        """Terminte program"""
        return True

TERMINATE = ("good_bye", "exit", ".")

if __name__ == "__main__":
    cli = AddressBookInterface()
    print("Hello! Following commands are possible:")
    print(" - add_contact: Creates new contact")
    print(" - find_contact: Searches for given contact")
    print(" - show_all: Shows complete adress book")
    print(" - del_contact: Deletes phone number")
    print(" - edit_phone: Changes phone number")
    print(" - del_phone: Deletes phone number")
    print(" - exit: Terminates the program")
    while True:
        command = input(">>> ").strip()
        if command == "add_contact":
            cli.cli_add_contact("")
        elif command == "find_contact":
            cli.cli_find_contact("")
        elif command == "show_all":
            cli.cli_show_all("")
        elif command == "del_contact":
            cli.cli_del_contact("")
        elif command == "edit_phone":
            cli.cli_edit_phone("")
        elif command == "del_phone":
            cli.cli_del_phone("")
        elif command in TERMINATE:
            print("Good Bye!")
            break
        else:
            print("Unknown command. \n- add_contact\n- find_contact\n- show_all\n- del_contact\n- edit_phone\n- del_phone\n- exit")