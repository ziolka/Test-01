path = 'users.csv'
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}


def save_credentials_users(path, users_info):
    print(path)
    print(users_info)
    with open(path, 'wb') as f1:
        for k, v in users_info.items():
            # print(f'{k}:{v}')
            line = f'{k}:{v}\n'
            print(line)
            byte_str = line.encode()
            print(byte_str)
            f1.write(byte_str)

print(save_credentials_users(path, users_info))