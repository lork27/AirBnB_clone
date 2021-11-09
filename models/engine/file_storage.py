#!/usr/bin/python3
'''module that contains FileStorage class'''


class FileStorage:
    __file_path = "placeholder for path"
    __objects = {}

    def all(self):
        '''
        public method that returns the dictionary of __objects
        '''
        return {}

    def new(self, obj):
        '''
        sets in _objects the obj with <obj classname>.id
        '''
        # add to __dict key obj.__name__ + obj.id and value as the object itself

    def save(self):
        '''
        serializes __objects to the JSON file path:__file_path
        '''
        # json serialization stuff here

    def reload(self):
        '''
        de-serializes JSON files to __objects
        '''
        # json deserialization stuff here
        # but only if it exists otherwise do nothing
