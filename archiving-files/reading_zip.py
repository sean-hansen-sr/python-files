import zipfile

def read_zip(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as archive:
        lst = archive.namelist()
        for l in lst:
            zfinf = archive.getinfo(l)
            print(f"{l} => {zfinf.file_size} bytes, compressed to {zfinf.compress_size} bytes")

read_zip('./archive.zip')