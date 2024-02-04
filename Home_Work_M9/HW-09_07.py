def normal_name(list_name):
    print(list_name)
    for i in list(map(lambda item: item.title(), list_name)):
    
        print(i)
        list_name.pop(0)
        list_name.append(i)
    print(list_name)
    return list_name