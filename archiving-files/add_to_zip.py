import zipfile

to_add = ['./files/01_file.csv',
          './files/01_file.txt',]

def add_to_zip(zip_filename, files, opt):
    with zipfile.ZipFile(zip_filename, opt) as archive:
        for file in files:
            lst = archive.namelist()
            if not file in lst:
                archive.write(file)
            else:
                print(f'File {file} already exists in the archive.')


add_to_zip('./archive.zip', to_add, 'a')
