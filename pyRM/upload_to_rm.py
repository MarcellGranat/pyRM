import os
import re
from time import sleep
import subprocess

def files_in_folder(rm_folder = None, path_to_rmapi = "/Users/marci/Downloads/rmapi-2"):
    if rm_folder:
        command = f"{path_to_rmapi} ls {rm_folder}"
    else:
        command = f"{path_to_rmapi} ls"
    existing_files_string = os.popen(command).read()
    existing_files = [re.sub("\[f\]\\t", "", _) for _ in existing_files_string.split("\n") if _ != '' and _.startswith("[f]")]
    return existing_files


def upload_to_rm(filename, rm_folder = None, path_to_rmapi = "/Users/marci/Downloads/rmapi-2"):
    full_path = os.path.abspath(filename)
    folder_path = os.path.dirname(full_path)
    filename = os.path.basename(full_path)
    put_command = f"put {filename}"
    if rm_folder:
        put_command = put_command + f" /{rm_folder}"
    command = f"cd {folder_path}; {path_to_rmapi} {put_command}; exit;"
    value = subprocess.run((command), shell = True)
    existing_files = files_in_folder(rm_folder = rm_folder, path_to_rmapi = path_to_rmapi)
    sleep(2)
    if filename in existing_files:
        return value.returncode == 0
    else:
        if filename.removesuffix(".pdf") in existing_files: # wihtout the extension
            return value.returncode == 0
        else:
            raise InterruptedError("File not found in folder after upload process.")

if __name__ == "__main__":
    filename = "api_testing.pdf"
    upload_to_rm(filename, rm_folder="books")
