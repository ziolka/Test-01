import shutil


def create_backup(path, file_name, employee_residence):
    print(path)
    print(file_name)
    print(employee_residence)
    file_path = f'{path}/{file_name}'
    print(file_path)
    with open(file_path, 'wb') as f1:
        for key, value in employee_residence.items():
            # print(key + " "+  value)
            line = f'{key} {value}\n'
            print(line)
            byte_line = line.encode('utf-8')
            print(byte_line)
            f1.write(byte_line)

    archive_name = shutil.make_archive('backup_folder', 'zip', path)
    return archive_name    