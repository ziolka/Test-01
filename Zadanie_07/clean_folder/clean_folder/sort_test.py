import os, shutil, sys
from clean_folder.rename_files import rename_files, rename_dirs
from clean_folder.create_folder_structure import create_folder_structure
from clean_folder.sort_files import sort_files
from clean_folder.remove_empty_folders import remove_empty_folders
from clean_folder.create_lists import file_list, ext_list
from clean_folder.unpack_archives import unpack_archives
from pathlib import Path

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Very useful file sorter")
    parser.add_argument('path', help='Folder path')
    return parser.parse_args()


# parser = argparse.ArgumentParser(description='Folder path input')

# # -i is argument name, dest is where it will be saved inside the parsed arguments Namespace
# parser.add_argument('-i', dest='folder_path', help = 'Path to input folder')

# args = parser.parse_args()

# print('Parsed folder path: ', args.folder_path)

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

# folder_path = Path(args.folder_path)
# # folder_path = sys.argv[1]
# # folder_path = Path(sys.argv[1])
# print(f'Folder path: {folder_path}')

def main():
    print("This is begining of the MAIN script")

    args = parse_args()
    folder_path = args.path
    # Tutaj możesz użyć zmiennej 'path'
    
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




# if __name__ == '__main__':
#     main(folder_path)