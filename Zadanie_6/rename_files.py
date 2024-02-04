import os
from normalize_name import normalize_name
import constants

def rename_files(folder_path):
    ''' 
    Rekursywnie zmienia nazwy plików 
    (przeszukuje także zagnieżdżone katalogi). 
    '''
    
    for file in os.listdir(folder_path):
        os.chdir(folder_path)
        if os.path.isfile(file):
            new_file_name = normalize_name(file)
            os.rename(file, new_file_name)
            print("***")
        else:
            nested_path = f'{folder_path}/{file}'
            print(f'New path: {nested_path}')
            rename_files(nested_path)

def rename_dirs(folder_path):
    ''' 
    Rekursywnie zmienia nazwy katalogów 
    (przeszukuje także zagnieżdżone katalogi). 
    Uwaga: Wywoływać dopiero po funkcji rename_files().
    '''
    for file in os.listdir(folder_path):
        os.chdir(folder_path)
        if os.path.isdir(file):
            new_dir_name = normalize_name(file)
            if file != new_dir_name:
                print(f'Old dir name: {file}')
                print(f'New dir name: {new_dir_name}')
                os.rename(file, new_dir_name)
                print("+++")
            nested_dir = f'{folder_path}/{new_dir_name}'
            print(f' Nested dir: {nested_dir}')
            rename_dirs(nested_dir)

    
if __name__ == '__main__':
    rename_files(constants.PATH)
    rename_dirs(constants.PATH)