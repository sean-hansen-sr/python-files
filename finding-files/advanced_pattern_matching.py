import os, fnmatch

def match(fld, search_pattern):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search_pattern):
            print(fn)

#match('./files', '*_file*.*')
#match('./files', '*_file_*.*')
match('./files', '*2_*_*.*')
