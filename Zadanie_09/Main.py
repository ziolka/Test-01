""""Home Work 9 - Personal Asistant"""

TERMINATE = ("good_bye", "exit", ".")
contacts = {}

def hello():
    return f"Hello! I am your bot. What do you want to do?:\n- add_contact\n- change_contact\n- get_phone_number\n- show_all\n- exit"

def add_contact(name="...", number="..."):
    contacts.update({name: number})
    return f"Following contact has been added: {name} with number: {number}"

def change_contact(name, new_number):
    contacts.update({name: new_number})
    return f"New phone number for {name} is: {new_number}"

def get_phone_number(name):
    return f"Phone number of {name} is {contacts.get(name)}"

def show_all():
    return contacts

def good_bye():
    return f"Good bye!"

command_handlers = {
    "hello": hello,
    "add_contact": add_contact,
    "change_contact": change_contact,
    "get_phone_number": get_phone_number,
    "show_all": show_all,
    "good_bye": good_bye,
    "exit": good_bye,
    ".": good_bye
}

""" Decorator """  
def input_error(command_parser):
    def inner(command):
        try:
            result = command_parser(command)
        except KeyError:
            print("Incorrect command")
        return result
    return inner

""" Task parser """
@input_error
def command_parser(command):
    command_parts = command.split(" ")
    command_parts[0] = command_parts[0].lower()
    if len(command_parts) == 1:
        return command_parts[0], None
    else:
        return command_parts[0], command_parts[1:]
    
""" Request-Answer loop """
def main():
    while True:
        command = input(">>>: ")
        if command in TERMINATE:
            break
        task, args = command_parser(command)
        if not args:
            print(command_handlers[task]())
        else:
            print(command_handlers[task](*args))   

    

if __name__ == '__main__':
    main()
