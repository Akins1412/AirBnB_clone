#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        damo1 = BaseModel()
        damo2 = BaseModel()
        self.assertNotEqual(damo1.id, damo2.id)

    def test_two_models_different_created_at(self):
        damo1 = BaseModel()
        sleep(0.05)
        damo2 = BaseModel()
        self.assertLess(damo1.created_at, damo2.created_at)

    def test_two_models_different_updated_at(self):
        damo1 = BaseModel()
        sleep(0.05)
        damo2 = BaseModel()
        self.assertLess(damo1.updated_at, damo2.updated_at)

    def test_str_representation(self):
        datetime = datetime.today()
        datetimerep = repr(datetime)
        damo = BaseModel()
        damo.id = "123456"
        damo.created_at = damo.updated_at = datetime
        damostr = damo.__str__()
        self.assertIn("[BaseModel] (123456)", damostr)
        self.assertIn("'id': '123456'", damostr)
        self.assertIn("'created_at': " + datetimerep, damostr)
        self.assertIn("'updated_at': " + datetimerep, damostr)

    def test_args_unused(self):
        damo = BaseModel(None)
        self.assertNotIn(None, damo.__dict__.values())

    def test_instantiation_with_kwargs(self):
        datetime = datetime.today()
        datetime_iso = dt.isoformat()
        damo = BaseModel(id="345", created_at=datetime_iso, updated_at=datetime_iso)
        self.assertEqual(damo.id, "345")
        self.assertEqual(damo.created_at, datetime)
        self.assertEqual(damo.updated_at, datetime)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        datetime = datetime.today()
        datetime_iso = dt.isoformat()
        damo = BaseModel("12", id="345", created_at=datetime_iso, updated_at=datetime_iso)
        self.assertEqual(damo.id, "345")
        self.assertEqual(damo.created_at, datetime)
        self.assertEqual(damo.updated_at, datetime)


class TestBaseModel_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        damo = BaseModel()
        sleep(0.05)
        first_updated_at = damo.updated_at
        damo.save()
        self.assertLess(first_updated_at, damo.updated_at)

    def test_two_saves(self):
        damo = BaseModel()
        sleep(0.05)
        first_updated_at = damo.updated_at
        damo.save()
        second_updated_at = damo.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        damo.save()
        self.assertLess(second_updated_at, damo.updated_at)

    def test_save_with_arg(self):
        damo = BaseModel()
        with self.assertRaises(TypeError):
            damo.save(None)

    def test_save_updates_file(self):
        damo = BaseModel()
        damo.save()
        damoid = "BaseModel." + damo.id
        with open("file.json", "r") as f:
            self.assertIn(damoid, f.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        damo = BaseModel()
        self.assertTrue(dict, type(damo.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        damo = BaseModel()
        self.assertIn("id", damo.to_dict())
        self.assertIn("created_at", damo.to_dict())
        self.assertIn("updated_at", damo.to_dict())
        self.assertIn("__class__", damo.to_dict())

    def test_to_dict_contains_added_attributes(self):
        damo = BaseModel()
        damo.name = "Holberton"
        damo.my_number = 98
        self.assertIn("name", damo.to_dict())
        self.assertIn("my_number", damo.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        damo = BaseModel()
        damo_dict = damo.to_dict()
        self.assertEqual(str, type(damo_dict["created_at"]))
        self.assertEqual(str, type(damo_dict["updated_at"]))

    def test_to_dict_output(self):
        datetime = datetime.today()
        damo = BaseModel()
        damo.id = "123456"
        damo.created_at = damo.updated_at = datetime
        todict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': datetime.isoformat(),
            'updated_at': datetime.isoformat()
        }
        self.assertDictEqual(damo.to_dict(), todict)

    def test_contrast_to_dict_dunder_dict(self):
        damo = BaseModel()
        self.assertNotEqual(damo.to_dict(), damo.__dict__)

    def test_to_dict_with_arg(self):
        damo = BaseModel()
        with self.assertRaises(TypeError):
            damo.to_dict(None)


if __name__ == "__main__":
    unittest.main()
