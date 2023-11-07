#!usr/bin/python3
"""Test BaseModel Class"""

from datetime import datetime
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """
    The test suite for models.base_model.BaseModel
    """

    def test_if_BaseModel_instance_has_id(self):
        """
        Checks that instance has an id assigned on initialization
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))

    def test_ids_is_unique(self):
        """
        Checks if id is generated randomly and uniquely
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_type_of_id_is_str(self):
        """
        Checks that id generated is a str object
        """
        b = BaseModel()
        self.assertTrue(type(b.id) is str)

    def test_created_at_is_datetime(self):
        """
        Checks that the attribute 'created_at' is a datetime object
        """
        b = BaseModel()
        self.assertTrue(type(b.created_at) is datetime)

    def test_updated_at_is_datetime(self):
        """
        Checks that the attribute 'updated_at' is a datetime object
        """
        b = BaseModel()
        self.assertTrue(type(b.updated_at) is datetime)

if __name__ == '__main__':
    unittest.main()