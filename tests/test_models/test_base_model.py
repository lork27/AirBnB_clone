#!/usr/bin/python3
"""
Unittest module for BaseModel Class
"""
from datetime import datetime
import unittest
from unittest.case import _AssertRaisesContext
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Class test BaseModel class"""

    def setUp(self):
        ''' create two base models'''
        self.A_base_model = BaseModel()
        self.B_base_model = BaseModel()

    def test_str(self):
        ''' Test __str__ method '''

    def test_Init(self):
        ''' Checks if Init works'''
        self.assertIsInstance(self.A_base_model, BaseModel)
        self.assertIsInstance(self.B_base_model, BaseModel)

    def test_Id(self):
        ''' Test if each instance have an unique id '''
        self.assertNotEqual(self.A_base_model.id,
                            self.B_base_model.id)

    def test_id_str(self):
        '''test if id is str'''
        self.assertIsInstance(self.A_base_model.id, str)

    def test_date_is_date(self):
        '''test if dates are datetime type'''
        self.assertIsInstance(self.A_base_model.created_at, datetime)
        self.assertIsInstance(self.A_base_model.updated_at, datetime)

    def test_date_update(self):
        '''test if datetimes updates correctly'''
        self.A_base_model.save()
        self.assertNotEqual(self.A_base_model.created_at,
                            self.A_base_model.updated_at)


if __name__ == "__main__":
    unittest.main()
