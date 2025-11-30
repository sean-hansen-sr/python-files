import csv

def read_csv(file_path, delimiter):
    with open(file_path) as csvfile:
        cnt = -1
        rows = csv.reader(csvfile, delimiter=delimiter)
        for row in rows:
            if cnt == -1:
                print(f'{" | ".join(row)}')
            else:
                print(f'{row[0]} | {row[1]} | {row[2]} | {row[3]}')
            cnt += 1
        print(f'{cnt} lines')

def write_csv(file_path, header, row):
    with open(file_path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(row)

if __name__ == "__main__":
    #read_csv('./files_to_read/names.csv', ',')
    write_csv('./files_to_read/names2.csv', 
              ['name', 'lastname', 'age', 'sex'], 
              ['Foo', 'Fighter', '82', 'male'])
