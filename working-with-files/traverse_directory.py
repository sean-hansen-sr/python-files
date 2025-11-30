import os

def traverse(fldr_path):
    for fldpath, dirs, fls in os.walk(fldr_path):
        print(f"Current folder path: {fldpath}")
        for fn in fls:
            print(f"\t{fn}")

traverse('./files')