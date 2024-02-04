import os
import shutil

def remove_empty_folders(folder_path):
    '''Removes folders other than known folders listed in the tuple.
       Use only at the end (after file sorting).
    '''

    known_folders = ("images", "documents", "audio", "video", "archives", "others")

    print(f'Received folder path: {folder_path}')
    print(f'CWD: {os.getcwd()}')
    os.chdir(folder_path)
    print(f'CWD after CHDIR: {os.getcwd()}')
    
    for file in os.listdir(folder_path):
            # print(f'Path: {path}')
            os.chdir(folder_path) 
            
            if os.path.isdir(file) and file not in known_folders:
                shutil.rmtree(file)
                print("---folder removed---")
               
if __name__ == '__main__':
    remove_empty_folders('D:/Python/Bałagan')