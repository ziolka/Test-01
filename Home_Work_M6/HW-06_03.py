def read_employees_from_file(path):
     
    list = []
    fh = open(path, 'r')
    while True:
        line = fh.readline()
        line = line.replace("\n", "")
        if not line:
            break
        print(line)
        list.append(line)
        print(list)
        
    fh.close()
    return list
    
    
