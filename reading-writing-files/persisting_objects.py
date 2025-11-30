import pickle

class Person:
    age = 45
    name = "John Doe"
    kids = ['Pete', 'Lilly', 'Kate']
    employers = {'AWS': 2022, 'Microsoft': 2018, 'Google': 2015}
    shoe_sizes = (9, 10, 11)

def serialize(obj):
    pickled = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    print(f"Serialized object: \n{(pickled)}\n")
    return pickled

def deserialize(pickled):
    unpickled = pickle.loads(pickled)
    print(f"Deserialized \n{unpickled}\n")

def deserialize_employers(obj):
    unpickled = pickle.loads(obj)
    print(f"Deserialized employers: \n{unpickled.employers}\n")

def obj_to_file(obj, filename):
    with open(filename, 'wb') as file:
        pickle.dump(obj, file, protocol=pickle.HIGHEST_PROTOCOL)

def file_to_obj(filename, unpickled):
    with open(filename, 'rb') as file:
        unpickled = pickle.load(file)
        print(f"Deserialized from file \n{unpickled}\n")
        return unpickled
    
if __name__ == "__main__":
    #pickled = serialize(Person())
    #deserialize(pickled)
    #deserialize_employers(pickled)
    obj = obj_to_file(Person(), './files_to_read/person.xyz')
    unpickled = file_to_obj('./files_to_read/person.xyz', obj)