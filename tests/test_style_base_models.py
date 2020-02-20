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

    def test_dict_date(self):
        """ Test Dict Date """
        base1 = BaseModel()
        d = base1.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(type(d["created_at"]), str)

    def test_iso(self):
        """ Test Format iso """
        base1 = BaseModel()
        cre = upd = datetime.now()
        base1.created_at = cre
        base1.updated_at = upd
        d = base1.to_dict()
        self.assertEqual(d["created_at"], cre.isoformat())
        self.assertEqual(d["updated_at"], upd.isoformat())
