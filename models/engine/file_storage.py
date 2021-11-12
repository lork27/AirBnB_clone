'''module that contains FileStorage class'''
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''
        public method that returns the dictionary of __objects
        '''
        return self.__objects

    def new(self, obj):
        '''
        sets in _objects the obj with <obj classname>.id
        '''
        self.__objects[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        '''
        serializes __objects to the JSON file path:__file_path
        '''
        new_dict = {}
        with open(self.__file_path, 'w') as f:
            for k, v in self.__objects.items():
                new_dict[k] = v.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        '''
        de-serializes JSON files to __objects
        '''
        tmp_dict = {}
        try:
            with open(self.__file_path, 'r') as f:
                tmp_dict = json.loads(f.read())
                for k, v in tmp_dict.items():
                    self.__objects[k] = eval(v["__class__"])(**v)
        except IOError:
            pass
