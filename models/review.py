#!/usr/bin/python3
"""module that contains review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """review class that inherits from BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
