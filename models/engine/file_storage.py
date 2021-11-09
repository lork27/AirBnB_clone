#!/usr/bin/python3
'''module that contains FileStorage class'''
import json


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
        self.__object[obj.__class__.__name__ + '.' + obj.id] = obj

    def save(self):
        '''
        serializes __objects to the JSON file path:__file_path
        '''
        new_dict = {}
        with open(self.__file__path, 'w') as f:
            for k, v in self.__objects.items():
                new_dict[k] = v.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        '''
        de-serializes JSON files to __objects
        '''
        # json deserialization stuff here
        # but only if it exists otherwise do nothing
