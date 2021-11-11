#!/usr/bin/python3
'''module that contains base class'''

import uuid
from datetime import date, datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        '''init method for BaseModel'''
        if len(kwargs) == 0:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)
        else:
            del kwargs['__class__']
            kwargs['created_at'] = datetime.strptime(
                kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs['updated_at'] = datetime.strptime(
                kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        '''str representation of basemodel instance'''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    '''public instance methods'''

    def save(self):
        """
        method that updates the date and time in which
        an instance was updated
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary representation of object"""
        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
