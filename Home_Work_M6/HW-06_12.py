import base64


def encode_data_to_base64(data):
    print(f'Data: {data}')
    list = []
    for pair in data:
        print(pair)
        entry_bytes = pair.encode('utf-8')
        entry_base64 = base64.b64encode(entry_bytes)
        entry_message = entry_base64.decode('utf-8')
        list.append(entry_message)
        print(list)
    return list
    