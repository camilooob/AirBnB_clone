#!/usr/bin/python3
import unittest
import inspect
import pep8
from models.base_model import BaseModel
from datetime import datetime


class Test_base_models(unittest.TestCase):

    def test_id_base_model(self):
        """ Test ID Base Model """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertTrue(base1.id != base2)

    def test_date_time(self):
        """ Test Date Time """
        base1 = BaseModel()
        self.assertFalse(datetime.now() == base1.created_at)
