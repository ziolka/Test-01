import shutil


def unpack(archive_path, path_to_unpack):
    print(archive_path)
    print(path_to_unpack)

    shutil.unpack_archive(archive_path, path_to_unpack)