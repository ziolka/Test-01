def get_employees_by_profession(path, profession):
    # print(profession)
    list = []
    join = ""
    
    with open(path, 'r') as fh:
        txt = fh.readlines()
        
    for line in txt:
        result = line.find(profession)
        # print(result)
        if result >= 0:
            list.append(line)
    # print(list)
    for i in range(0, len(list)):
        list[i] = list[i].replace("\n", "")
        list[i] = list[i].replace(" ", "")
        list[i] = list[i].replace(profession, "")
        join = join + f' {list[i]}'
        join = join.lstrip()
        
    print(join)
    return join