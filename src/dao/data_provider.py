
import os
import mimetypes


FILES = "files"
FOLDER = "folder"
FILE_NAME = "file_name"
FILE_SIZE = "file_size"
FILE_TYPE = "file_type"


def get_files(folder):
    files = {
        FILES: [],
        FOLDER: folder
    }
    for file_name in os.listdir(folder):
        full_path = os.path.join(folder, file_name)
        file_info = {}
        file_info[FILE_NAME] = file_name
        if not os.path.isdir(full_path):
            file_info[FILE_SIZE] = os.path.getsize(full_path)
        else:
            file_info[FILE_SIZE] = "DIR"
        file_info[FILE_TYPE] = mimetypes.guess_type(full_path)[0]
        files[FILES].append(file_info)
    return files