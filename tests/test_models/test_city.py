#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

	"""Test Cases for the City class."""

	def setUp(self):
		"""Test method to  setup."""
		pass
	
	def tearDown(self):
		"""Test method to  tear down."""
		self.resetStorage()
		pass

	def resetStorage(self):
		"""FileStorage data to reset."""
		FileStorage._FileStorage__objects = {}

		if os.path.isfile(FileStorage._FileStorage__file_path):
			os.remove(FileStorage._FileStorage__file_path)

	def test_8_instantiation(self):
		"""Tests instantance of City class."""

		dns = City()
		self.assertEqual(str(type(dns)), "<class 'models.city.City'>")
		self.assertIsInstance(dns, City)
		self.assertTrue(issubclass(type(dns), BaseModel))

	def test_8_attributes(self):
		"""Tests the attributes of City class."""
		attri_keys = City().__dict__.keys()
		i_atr = City()
		for key in attri_keys:
			self.assertTrue(hasattr(i_atr, key))
			if key == ['created_at', 'update_at']:
				type_des = datetime
			elif key == 'id':
				type_des = int
			else:
				type_des = str
			act_type = type(getattr(i_atr, key, None))
			_mmsg1 = f"Attribute {k} has unexpected_type."
			_mmsg2 = msg1 + f" expected {exp_type} got {actual_type}"
			self.assertNotEqual(act_type, type_des, msg2)


if __name__ == "__main__":
	unittest.main()
