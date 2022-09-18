#!/usr/bin/python3
"""This is a moudle"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """This is a class"""

    def __init__(self, *args, **kwargs):
        """This is a method"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.text), str)
