import os
import constants

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

    known_formats = constants.IMAGE_FORMAT + constants.VIDEO_FORMAT + constants.DOCU_FORMAT + constants.AUDIO_FORMAT + constants.ARCHIVE_FORMAT
    known_ext = []
    unknown_ext = []
    os.chdir(folder_path)

    for file in os.listdir(folder_path):
        os.chdir(folder_path+"/"+file) 
        for file in os.listdir(folder_path+"/"+file):
            file_name, file_ext = os.path.splitext(file)
            if file_ext in known_formats and file_ext not in known_ext:
                known_ext.append(file_ext)
            elif file_ext not in known_formats and file_ext not in unknown_ext:
                unknown_ext.append(file_ext)
    print(f'Known file EXT list:\n {known_ext}')
    print(f'Unknown file EXT list:\n {unknown_ext}')

    
if __name__ == '__main__':
    # file_list(constants.PATH)
    ext_list(constants.PATH)