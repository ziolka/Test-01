import os
import constants

def create_folder_structure(path):
    '''
    Creates folde structure for sorted files.
    '''
    os.chdir(path)
    if not os.path.exists('images'):
        os.mkdir('images')
    if not os.path.exists('movies'):
        os.mkdir('video')
    if not os.path.exists('documents'):
        os.mkdir('documents')
    if not os.path.exists('music'):
        os.mkdir('audio')
    if not os.path.exists('archives'):
        os.mkdir('archives')
    if not os.path.exists('others'):
        os.mkdir('others')


if __name__ == '__main__':
    create_folder_structure(constants.PATH)