import os, shutil
import constants

def unpack_archives(folder_path):
    ''' 
    Unpacks archives in folder_path/archives. 
    '''
    archives_folder = folder_path + "/archives"
    os.chdir(archives_folder)
    print(f'Archives folder path: {os.getcwd()}')

    for file in os.listdir(archives_folder):
        file_name, file_ext = os.path.splitext(file)
        unpack_folder = f'{archives_folder}/{file_name}'
        print(unpack_folder)
        shutil.unpack_archive(file, unpack_folder)
        os.remove(file)


        
if __name__ == '__main__':
    unpack_archives(constants.PATH)