def get_credentials_users(path):
    print(path)
    list = []
    with open(path, 'rb') as f1:
        while True:
            line = f1.readline()
            if not line:
                break
            line = line.decode()
            line = line.replace("\n", "")   
            print(line)
            list.append(line)
        print(f'List: {list}')

    return list