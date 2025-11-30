import os, fnmatch

def match(fld, pattern):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, pattern):
            print(fn)

match('./files', '*1*_file.csv')