import os

def delete_file(file_path):
    if os.path.isfile(file_path):
        try:
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted.")
        except OSError as e:
            print(f"Error deleting file '{file_path}': {e.strerror}")
    else:
        print(f"Error: '{file_path}' is not a valid file.")

delete_file('./files/text.txt')