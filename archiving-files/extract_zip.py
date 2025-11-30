import zipfile

def extract_file(zip_path, fn, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as archive:
        archive.extract(fn, path=extract_to)

def extract_all(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as archive:
        archive.extractall(path=extract_to)

if __name__ == "__main__":
    #extract_file('./archive.zip', 'files/01_file_test.txt', 'extracted')
    extract_all('./archive.zip', 'extracted')