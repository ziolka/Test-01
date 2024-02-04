class IDException(Exception):
    pass


def add_id(id_list, employee_id):
    print(f'Employee ID: {employee_id}')
    if not employee_id.startswith("01"):
        raise IDException
    else:
        id_list.append(employee_id)
    print(f'ID list: {id_list}')
    return id_list
    
while True:
    try:
        add_id
        break
    except IDException:
        print("ID does not starts with 01")