import os
from .file_path import *

def upload_to_rm(filename, rm_folder = None, path_to_rmapi = "/Users/marci/Downloads/rmapi-2"):
    folder_path, file_name = file_path(filename)
    put_command = f"put {file_name}"
    if rm_folder:
        put_command = put_command + f" /{rm_folder}"
    print(put_command)
    command = f"cd {folder_path}; {path_to_rmapi} {put_command}; exit;"
    os.system(command)

if __name__ == "__main__":
    filename = "api_testing.pdf"
    upload_to_rm(filename, rm_folder="books")
