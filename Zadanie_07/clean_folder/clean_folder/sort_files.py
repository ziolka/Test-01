import os
import shutil

def sort_files(folder_path, root_folder_path):

    image_format = (".jpeg", ".png", ".jpg", ".svg", ".log")
    video_format = (".avi", ".mp4", ".mov", ".mkv")
    docu_format = (".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx")
    audio_format = (".mp3", ".ogg", ".wav", ".amr")
    archive_format = (".zip", ".gz", ".tar")
    known_folders = ("images", "documents", "audio", "video", "archives", "others")

    print(f'Received folder path: {folder_path}')
    print(f'CWD: {os.getcwd()}')
    os.chdir(folder_path)
    print(f'CWD after CHDIR: {os.getcwd()}')
    
    for file in os.listdir(folder_path):
            # print(f'Path: {path}')
            os.chdir(folder_path) 
            
            if os.path.isfile(file):
                print("---")
                file_name, file_ext = os.path.splitext(f'{root_folder_path}/{file}')
                if file_ext in image_format:
                    print(f'File with image format: {folder_path}/{file}')
                    shutil.move(file, f'{root_folder_path}/images')
                elif file_ext in docu_format:
                    print(f'File with docu format: {folder_path}/{file}')
                    shutil.move(file, f'{root_folder_path}/documents')
                elif file_ext in audio_format:
                    print(f'File with music format: {folder_path}/{file}')
                    shutil.move(file, f'{root_folder_path}/audio')
                elif file_ext in video_format:
                    print(f'File with video format: {folder_path}/{file}')
                    shutil.move(file, f'{root_folder_path}/video')
                elif file_ext in archive_format:
                    print(f'File with archive format: {folder_path}/{file}')
                    shutil.move(file, f'{root_folder_path}/archives')
                else:
                    print(f'File with other format: {folder_path}/{file}')
                    shutil.move(file, f'{root_folder_path}/others')

            elif os.path.isdir(file) and file not in known_folders:
                nested_path = f'{folder_path}/{file}'
                print(f'+++ New nested folder path: {nested_path}')
                sort_files(nested_path, root_folder_path)



                    
                                            


if __name__ == '__main__':
    sort_files('D:/Python/Bałagan', 'D:/Python/Bałagan')