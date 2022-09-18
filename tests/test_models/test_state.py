#!/usr/bin/python3
"""This is a module"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """This is a class"""

    def __init__(self, *args, **kwargs):
        """This is a method"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.name), str)
