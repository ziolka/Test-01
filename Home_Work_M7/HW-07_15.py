def flatten(data, flat_list=None):
    if flat_list is None:
        flat_list = []
    if len(data) == 0:
        return flat_list

    for i in range(0, len(data)):
        x = isinstance(data[0], list)
        print(x)
        if x == False:
            print(data[0])
            flat_list.append(data[0])
            print(f' flat list: {flat_list}')
            data.pop(0)
        else:
            sublist = data.pop(0)
            print(f' sublist {sublist}')
            for j in range (0, len(sublist)):
                flatten(sublist, flat_list)
    
    return flat_list          