def make_request(keys, values):
    print(keys)
    print(values)
    dict = {}
    index = 0
    if len(keys) != len(values):
        return dict
    for key in keys:
        print(key)
        print(values[index])
        dict[key] = values[index]
        index +=1
    print(dict)
    return dict
