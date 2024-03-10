#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):

	"""Test Cases for the State class."""

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
		"""Tests instantiation of State class."""

		dns = State()
		self.assertEqual(str(type(dns)), "<class 'models.state.State'>")
		self.assertIsInstance(dns, State)
		self.assertTrue(issubclass(type(dns), BaseModel))


if __name__ == "__main__":
	unittest.main()
