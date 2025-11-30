import json

def read_print_json(file_path, pretty, sort):
    with open(file_path) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, sort_keys=sort, indent=4 if pretty else None))

def update_author_json(file_path, arr_name, pos, key, value):
    with open(file_path, 'r') as read_file:
        data = json.load(read_file)
        data[arr_name][pos][key] = value
        with open(file_path, 'w') as write_file:
            json.dump(data, write_file, indent=4)

if __name__ == "__main__":  
    #read_print_json('./files_to_read/authors.json', False, False)
    update_author_json('./files_to_read/authors.json', 'authors', 1, 'courses', 10)