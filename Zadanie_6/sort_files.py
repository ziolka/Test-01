import os
import shutil
import constants

def sort_files(folder_path, root_folder_path):
    '''
    Sorts files into already created folders.
    '''
    print(f'Received folder path: {folder_path}')
    print(f'CWD: {os.getcwd()}')
    os.chdir(folder_path)
    print(f'CWD after CHDIR: {os.getcwd()}')
    
    for file in os.listdir(folder_path):
        os.chdir(folder_path) 
        
        if os.path.isfile(file):
            print("---")
            file_name, file_ext = os.path.splitext(root_folder_path+"/"+file)
            if file_ext in constants.DOCU_FORMAT:
                print(f'File with image format: {folder_path+"/"+file}')
                shutil.move(file, root_folder_path + "/images")
            elif file_ext in constants.IMAGE_FORMAT:
                print(f'File with docu format: {folder_path+"/"+file}')
                shutil.move(file, root_folder_path+"/documents")
            elif file_ext in constants.AUDIO_FORMAT:
                print(f'File with music format: {folder_path+"\\"+file}')
                shutil.move(file, root_folder_path+"/audio")
            elif file_ext in constants.VIDEO_FORMAT:
                print(f'File with video format: {folder_path+"\\"+file}')
                shutil.move(file, root_folder_path+"/video")
            elif file_ext in constants.ARCHIVE_FORMAT:
                print(f'File with archive format: {folder_path+"\\"+file}')
                shutil.move(file, root_folder_path+"/archives")
            else:
                print(f'File with other format: {folder_path+"\\"+file}')
                shutil.move(file, root_folder_path+"/others")

        elif os.path.isdir(file) and file not in constants.KNOWN_FOLDERS:
            nested_path = f'{folder_path}/{file}'
            print(f'+++ New nested folder path: {nested_path}')
            sort_files(nested_path, root_folder_path)



                    
                                            


if __name__ == '__main__':
    sort_files(constants.PATH, constants.PATH)