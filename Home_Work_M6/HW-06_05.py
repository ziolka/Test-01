def get_cats_info(path):
    print(f'Path: \n {path}')
    dict_list = []
    with open(path, 'r') as fh:
        while True:
            dict = {}
            record = fh.readline()
            record = record.replace("\n", "")
            if not record:
                break
            print(f'Record: {record}')
            values = record.split(",")
            print(f'Values: {values}')
            print(values[0])
            print(values[1])
            print(values[2])
            dict["id"] = values[0]
            dict["name"] = values[1]
            dict["age"] = values[2]
            print(f'Dict: {dict}')
            dict_list.append(dict)

    print(f'Ditionary List: \n{dict_list}')
                
    return dict_list
    



