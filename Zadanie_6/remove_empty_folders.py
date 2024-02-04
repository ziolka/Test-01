import os
import shutil
import constants

def remove_empty_folders(folder_path):
    '''Removes folders other than known folders listed in the tuple.
       Use only at the end (after file sorting).
    '''

    print(f'Received folder path: {folder_path}')
    print(f'CWD: {os.getcwd()}')
    os.chdir(folder_path)
    print(f'CWD after CHDIR: {os.getcwd()}')
    
    for file in os.listdir(folder_path):
        os.chdir(folder_path) 
        
        if os.path.isdir(file) and file not in constants.KNOWN_FOLDERS:
            shutil.rmtree(file)
            print("---folder removed---")
               
if __name__ == '__main__':
    remove_empty_folders(constants.PATH)