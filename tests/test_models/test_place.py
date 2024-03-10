#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
from datetime import datetime
import time
from models.place import Place
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

	"""Test Cases for the Place class."""

	def setUp(self):
		"""Test methods set up."""
		pass

	def tearDown(self):
		"""Test methods tear down."""
		self.resetStorage()
		pass

	def resetStorage(self):
		"""FileStorage data reset."""
		FileStorage._FileStorage__objects = {}
		if os.path.isfile(FileStorage._FileStorage__file_path):
			os.remove(FileStorage._FileStorage__file_path)

	def test_8_instantiation(self):
 		"""Tests instantiation of Place class."""

		dns = Place()
		self.assertEqual(str(type(dns)), "<class 'models.place.Place'>")
		self.assertIsInstance(dns, Place)
		self.assertTrue(issubclass(type(dns), BaseModel))


if __name__ == "__main__":
	unittest.main()
