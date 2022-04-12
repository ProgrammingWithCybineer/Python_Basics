#how to convert from python object to json data

import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

personJson = json.dumps(person, indent=4)
print(personJson)


# this created person.json file 
with open ('person.json', 'w') as file:
    json.dump(person, file, indent=4)
    
    

#Convert a JSON string into a Python object with the json.loads() method. The result will be a Python dictionary.    
person = json.loads(personJson)
print(person)


# load data from a file and convert it to a Python object with the json.load() method.
with open ('person.json', 'r') as file:
    person = json.load(file)
    print(person)
    
    
    
# We can specify a custom encoding function that will store the class name and all object variables in a dictionary.
# Use this function for the default argument in the json.dump() method. 
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
user = User('Max',27)

def encode_user(o):
    if isinstance(o, User):
        return{'name': o.name, 'age':o.age, o.__class__.__name__: True}
    else:
        return TypeError('Object of type User is not JSON serializable')

userJSON = json.dumps(user, default=encode_user)
print(userJSON)


#custom Encoder class, and overwrite the default() method. Use this for the cls argument in the json.dump() method, or use the encoder directly.
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
             return{'name': o.name, 'age':o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)
    
userJSON = UserEncoder().encode(user)
print(userJSON)



