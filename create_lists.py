import os
''' 
Creates file lists 
'''
def file_list(folder_path):
    images =[]
    documents = []
    audio = []
    video = []
    archives = []
    others = []
    for dir in os.listdir(folder_path):
        print(dir)
        os.chdir(folder_path+"/"+dir)
        if str(dir) == 'images':
           for file in os.listdir(os.getcwd()):
               images.append(file)
        elif str(dir) == 'documents':
           for file in os.listdir(os.getcwd()):
               documents.append(file)
        elif str(dir) == 'audio':
           for file in os.listdir(os.getcwd()):
               audio.append(file)
        elif str(dir) == 'video':
           for file in os.listdir(os.getcwd()):
               video.append(file)
        elif str(dir) == 'archives':
           for file in os.listdir(os.getcwd()):
               archives.append(file)
        elif str(dir) == 'others':
           for file in os.listdir(os.getcwd()):
               others.append(file)


    print(f'Image list:\n {images}')
    print(f'Document list:\n {documents}')
    print(f'Audio list:\n {audio}')
    print(f'Video list:\n {video}')
    print(f'Archive list:\n {archives}')
    print(f'Others list:\n {others}')


def ext_list(folder_path):
    image_format = [".jpeg", ".png", ".jpg", ".svg", ".log"]
    video_format = [".avi", ".mp4", ".mov", ".mkv"]
    docu_format = [".doc", ".docx", ".txt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
    audio_format = [".mp3", ".ogg", ".wav", ".amr"]
    archive_format = [".zip", ".gz", ".tar"]

    known_formats = image_format + video_format + docu_format + audio_format + archive_format
    # print(known_formats)
    known_ext = []
    unknown_ext = []
    os.chdir(folder_path)

    for file in os.listdir(folder_path):
        os.chdir(folder_path+"/"+file) 
        # print(os.getcwd())
        for file in os.listdir(folder_path+"/"+file):
            file_name, file_ext = os.path.splitext(file)
            if file_ext in known_formats and file_ext not in known_ext:
                known_ext.append(file_ext)
            elif file_ext not in known_formats and file_ext not in unknown_ext:
                unknown_ext.append(file_ext)
    print(f'Known file EXT list:\n {known_ext}')
    print(f'Unknown file EXT list:\n {unknown_ext}')

    
if __name__ == '__main__':
    # file_list('D:/Python/Bałagan')
    ext_list('D:/Python/Bałagan')