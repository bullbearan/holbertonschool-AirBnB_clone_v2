#!/usr/bin/python3
"""This is a module"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """This is a class"""

    def __init__(self, *args, **kwargs):
        """This is a method"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.name), str)
