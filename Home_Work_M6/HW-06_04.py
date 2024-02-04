def add_employee_to_file(record, path):
    print(f'Record: \n {record} \nPath: \n {path}')
    f = open(path, 'a')
    f.write(record + '\n')

    f.close()
    
    
    
    
