# Task parser

def add_number(name, number):
    print(f"[name {name} and number {number} saved]")
    return f"{name} number has been saved!"


# Command handlers

command_handlers = {
    "add_number": add_number,
    "sub_number": sub_number,
    "mul_number": mul_number,
    "div_number": div_number,


}


# Request-Answer loop

while True:
    command = input("$: ")
    command_parts = command.split(" ")
    instruction = command_parts[0]
    args = command_parts[1:]
    print(command_handlers[instruction](*args))
    