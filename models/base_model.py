#!/usr/bin/python3
'''module that contains base class'''

import uuid
from datetime import date, datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        '''init method for BaseModel'''
        # not sure about updated_at being assigned at every instance
        # maybe that can be left for when save method is saved
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
        """
        public method that returns dictionary
        representation of instance
        """
        return {
            # 'my_number': self.my_number,
            'name': self.name,
            '__class__': self.__class__.__name__,
            'updated_at': self.updated_at.isoformat(),
            'id': self.id,
            'created_at': self.created_at.isoformat()
        }

    # we may need to update to_dict() method so is not as 'hardcoded'
    # possible way is looping thru all properties so it takes into account
    # added in attributes such as name, my_number, etc.
    '''
    def to_dict(self):
        """Retorna un dictionario que contenga todos los keys/values de dict"""
        dict_returned = dict(self.dict)
        dict_returned["created_at"] = self.created_at.isoformat()
        dict_returned["updated_at"] = self.updated_at.isoformat()
        dict_returned["class"] = self.class.name
        return dict_returned
    '''
