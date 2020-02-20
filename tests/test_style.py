#!/usr/bin/python3
import unittest
import inspect
import pep8
from models import base_model, amenity, place, review, city, user, state


class Test_All_Files(unittest.TestCase):

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py',
                                        'models/engine/file_storage.py',
                                        'models/amenity.py',
                                        'models/city.py',
                                        'models/review.py',
                                        'models/state.py',
                                        'models/place.py',
                                        'models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def test_all_class(cls):
        cls.base_model = inspect.getmembers(base_model, inspect.isfunction)
        cls.amenity = inspect.getmembers(amenity, inspect.isfunction)
        cls.place = inspect.getmembers(place.Place, inspect.isclass)
        cls.review = inspect.getmembers(review, inspect.ismodule)
        cls.city = inspect.getmembers(city, inspect.isfunction)
        cls.state = inspect.getmembers(state, inspect.isfunction)
        cls.user = inspect.getmembers(user.User, inspect.isclass)

    def test_functions_classes(self):
        for i in self.base_model:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.amenity:
            self.assertTrue(len(i[1].__doc) > 0)
        for i in self.city:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.place:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.review:
            self.assertTrue(len(i[1].__doc__) > 0)
        for i in self.state:
            self.assertTrue(len(i[1].__doc__) > 0)

    def test_module_documentation(self):
        self.assertTrue(len(amenity.__doc__) > 0)
        self.assertTrue(len(base_model.__doc__) > 0)
        self.assertTrue(len(city.__doc__) > 0)
        self.assertTrue(len(place.__doc__) > 0)
        self.assertTrue(len(review.__doc__) > 0)
        self.assertTrue(len(state.__doc__) > 0)
