import zipfile

to_zip = ['./files/subfolder/01_file_test.csv',
          './files/subfolder/01_file_test.txt',
          './files/subfolder/01_test_file.csv',
          './files/subfolder/01_test_file.txt',
          './files/01_file_test.csv',
          './files/01_file_test.txt']

def create_zip(zip_filename, file_list, opt):
    with zipfile.ZipFile(zip_filename, opt, allowZip64=True) as archive:
        for file in file_list:
            archive.write(file)

create_zip('./archive.zip', to_zip, 'w')