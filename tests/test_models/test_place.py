#!/usr/bin/python3
"""This is a module"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """This is a class"""

    def __init__(self, *args, **kwargs):
        """This is a method"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """This is a method"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
