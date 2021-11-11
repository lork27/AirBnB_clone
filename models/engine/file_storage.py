'''module that contains FileStorage class'''
import json
from models.base_model import BaseModel
# this import is a placeholder so our placeholder
# placholder can placeholder while placeholding


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
        print(self.__objects)
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
                    '''
                    module = __import__(models.v["__class__"])
                    class_ = getattr(module, v["__class__"])
                    self.__objects[k] = class_(**v)
                    '''
                    self.__objects[k] = BaseModel(**v)
                    # this is a hack, hardcoded, no bueno
        except IOError:
            pass
