def read_txt(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        print(f.read())

def read_txt_by_line(fname):
    with open(fname, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
            line = f.readline()

def write_new_txt(fname, content):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

def append_txt(fname, content):
    with open(fname, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(content)


if __name__ == "__main__":
    #read_txt('./files_to_read/backup.py')
    #read_txt_by_line('./files_to_read/backup.py')
    #write_new_txt('./files_to_read/example.txt', 'This is a test....')
    append_txt('./files_to_read/example.txt', 'This is an appended line.')