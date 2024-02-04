def file_operations(path, additional_info, start_pos, count_chars):
    print(path)
    print(additional_info)
    print(start_pos)
    print(count_chars)
    with open(path, 'a') as fh:
        fh.seek(start_pos)
        fh.write(additional_info)
        
    with open(path, 'r') as fh:
        fh.readlines()