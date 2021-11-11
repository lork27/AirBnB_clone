#!/usr/bin/python3
'''module that contains user subclass'''

from models.base_model import BaseModel


class User(BaseModel):
    '''User class'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
