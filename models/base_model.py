#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents  BaseModel of  HBnB project."""

	def __init__(self, *args, **kwargs):
	"""Initialize  new BaseModel.

	Args:
	*args (any): Unused arguments.
		**kwargs (dict): Key/value args.
	"""

	self.id = str(uuid4())
	self.created_at = datetime.now()
	self.updated_at = datetime.now()
	date_now = "%Y-%m-%dT%H:%M:%S.%f"
	if len(kwargs) != 0:
		for ke, value in kwargs.items():
			if ke == "created_at" or ke == "updated_at":
				self.__dict__[ke] = datetime.strptime(value, date_now)
		else:
			self.__dict__[ke] = value
	else:
		models.storage.new(self)

	def save(self):
	"""Update 'updated_at' with recent datetime."""
	self.updated_at = datetime.now()
	models.storage.save()

	def __str__(self):
	"""Return the print/str represent."""
	cls_name = self.__class__.__name__
	return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

	def to_dict(self):
	"""Return the dictionary.

	Includes key/value pair __class__ representing
	the class name of the object.
	"""
	ob_dict = self.__dict__.copy()
	ob_dict["created_at"] = self.created_at.isoformat()
	ob_dict["updated_at"] = self.updated_at.isoformat()
	ob_dict["__class__"] = self.__class__.__name__
	return ob_dict
