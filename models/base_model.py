#!/usr/bin/python3
'''module that contains base class'''
import json
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        '''init method for BaseModel'''
        if kwargs is not None:
            if 'name' in kwargs:
                self.name = kwargs["name"]
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'id' in kwargs:
                self.id = kwargs['id']
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())

    def __str__(self):
        '''str representation of basemodel instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    '''public instance methods'''

    def save(self):
        """
        method that updates the date and time in which
        an instance was updated
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        public method that returns dictionary
        representation of instance
        """
        return {
            'my_number': self.my_number,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }
