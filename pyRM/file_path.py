import pyhere

def main(file_path):
    full_path = pyhere.here(file_path)
    folder_parts = list(full_path.parts[1:-1])
    folder_path = "/" + "/".join(folder_parts)
    file_name = full_path.parts[-1]
    return folder_path, file_name

if __name__ == "__main__":
    file_path = "README.md"
    print(main(file_path))


