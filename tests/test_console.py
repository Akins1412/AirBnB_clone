#!/usr/bin/python3
"""Module for testing the HBNBCommand Class"""
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class Test_Console(unittest.TestCase):
	"""Test the HBNBCommand Console"""
	def test_help(self):
		"""Tests the help command."""
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("help")
		_j = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n
"""
		self.assertEqual(_j, f.getvalue())

	# Test cases for quit

	def test_do_quit(self):
	"""Test quit commmand"""
	with patch('sys.stdout', new=StringIO()) as f:
		HBNBCommand().onecmd("quit")
	# modelling what happens when someone types `quit`
	note = f.getvalue()
	self.assertTrue(len(note) == 0)
	self.assertEqual("", note)

	with patch('sys.stdout', new=StringIO()) as f:
		HBNBCommand().onecmd("quit garbage")
	# modelling when user types `quit anything`
	note = f.getvalue()
	self.assertTrue(len(note) == 0)
	self.assertEqual("", note)

	# Test cases for EOF
	def test_do_EOF(self):
		"""Test EOF commmand"""
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("EOF")
		# modelling what happens when user types `quit`
		note = f.getvalue().strip().split('\n')
		# self.assertTrue(len(msg) == 1)
		_info = f"Expected length 1, got{len(msg)}.\nOutput:{msg}"
		self.assertEqual(len(note), 1, _info)

	# Test cases for emptyline
	def test_do_emptyline(self):
		"""Test emptyline command"""
		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("\n")
		# modelling what happens when user doesn't type anything
		note = f.getvalue()
		self.assertTrue(len(note) == 0)
		self.assertEqual("", note)

		with patch('sys.stdout', new=StringIO()) as f:
			HBNBCommand().onecmd("                     \n")
		# modelling when user types lots of whitespaces & enter
		note = f.getvalue()
		self.assertTrue(len(note) == 0)
		self.assertEqual("", note)

	# Test cases for do_all
	def test_do_all(self):
		"""Test do_all command"""
		with patch('sys.stdout', new=StringIO()) as f:
			 HBNBCommand().onecmd("all")

	# Test cases for do_count
	# Test cases for do_show
	# Test cases for do_create
	# Test cases for do_update
	# Test cases for do_destroy


if __name__ == "__main__": 
	unittest.main()
