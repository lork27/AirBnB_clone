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
        with open(self.__file_path, 'w') as f:
            for k, v in self.__objects.items():
                new_dict[k] = v.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        '''
        de-serializes JSON files to __objects
        '''
        '''
        try: open __file_path
        except do nothing
        de-serialize (json.loads) JSON file to tmp_dict
            tmp_dict is now a nested dictionary and we want to create an instance for every dictionary within
        loop through every item in tmp_dict and create an instance
            key[:-16](**value)??? -16 because we store name and id(uuid) of every instance and uuid is 16 chars long afaik
        
        
        '''
        # but only if it exists otherwise do nothing
