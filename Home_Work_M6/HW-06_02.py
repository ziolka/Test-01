def write_employees_to_file(employee_list, path):
    print(f'Employee List: \n {employee_list}')
    print(f'Path: \n {path}')
    
    fh = open(path, 'w')
    for department in employee_list:
        for employee in department:
            print(f'Employee: {employee}')
            fh.write(employee + '\n')

    fh.close() 
   
        