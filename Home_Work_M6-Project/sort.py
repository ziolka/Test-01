import os, shutil
from rename_files import rename_files, rename_dirs
from create_folder_structure import create_folder_structure
from sort_files import sort_files
from remove_empty_folders import remove_empty_folders
from create_lists import file_list, ext_list
from unpack_archives import unpack_archives

def sort(folder_path):
    root_folder_path = folder_path 
    os.chdir(folder_path)
    rename_files(folder_path)
    rename_dirs(folder_path)
    create_folder_structure(folder_path)
    sort_files(folder_path, root_folder_path)
    remove_empty_folders(folder_path)
    file_list(folder_path)
    ext_list(folder_path)
    unpack_archives(folder_path)




if __name__ == '__main__':
    sort('D:/Python/Bałagan')