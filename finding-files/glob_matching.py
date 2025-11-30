from pathlib import Path

def glob_match(fld, search_pattern):
    p = Path(fld)
    for n in p.glob(search_pattern):
        print(n)

#glob_match('./files', '*2*.t*')
glob_match('./files/subfolder', '*_file_*.t*')