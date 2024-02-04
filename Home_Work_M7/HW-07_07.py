def data_preparation(list_data):
    result = []
    for list in list_data:
        list.sort()
        if len(list) >= 2:
            x = list.pop(0)
            list_len = len(list)-1
            y = list.pop(list_len)
    
    for list in list_data:
        result.extend(list)
        result.sort()
        result.reverse()
    return result