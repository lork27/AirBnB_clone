#!/usr/bin/python3
"""Module that contains City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """state class than inherits from BaseModel"""
    state_id = ""
    name = ""
