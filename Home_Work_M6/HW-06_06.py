def get_recipe(path, search_id):
    dict  = {}
    with open(path, 'r') as fh:
        while True:
            dict = {}
            record = fh.readline()
            record = record.replace("\n", "")
            # print(f'Record: {record}')
            if not record:
                break
            entry = record.split(",")
            print(f'Entry: {entry}')
            search = entry[0].find(search_id)
            print(f'Search result: {search}')
            if search == -1:
                return None
            else:
                dict["id"] = entry[0]
                print(f'Entry_0: {entry[0]}')
                dict["name"] = entry[1]
                print(f'Entry_1: {entry[1]}')
                dict["ingredients"] = entry[2:]
                print(f'Entry_2: {entry[2:]}')

                print(f'Receipe: \n{dict}')
                
                return dict