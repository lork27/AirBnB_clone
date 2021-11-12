#!/usr/bin/python3
"""
Unittest module for BaseModel Class
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Class test BaseModel class"""

    def test_init(self):
        """test init method of BaseModel"""
        test_model = BaseModel()
        message = "Object is not instance of class"
        self.assertIsInstance(test_model, BaseModel, message)


if __name__ == "__main__":
    unittest.main()
