#!/usr/bin/python3
'''module that contains base class'''
import json
import uuid
import datetime


class BaseModel:
    def __init__(self, name=None, my_number=None, id=None):
        '''init method for BaseModel'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        self.name = name
        self.my_number = my_number

    # str should print [<class name>] (<self.id>) <self.__dict__>
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
