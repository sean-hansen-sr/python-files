import os

def ends_with(fld, search_str):
    for fn in os.listdir(fld):
        if fn.endswith(search_str):
            print(fn)

def starts_with(fld, search_str):
    for fn in os.listdir(fld):
        if fn.startswith(search_str):
            print(fn)

#ends_with("./files", ".txt")
starts_with("./files", "01_test")