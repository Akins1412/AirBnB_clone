#!/usr/bin/python3
""" common attributes/methods that defines BaseModel"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
	""" Backbone represented for all other clasess
		common attributes/methods that defines BaseModel
	"""

def __init__(self, *args, **kwargs):
	"""Initialize new Basemodel
	Args:
	*args: list argument
	**kwargs: key/valus of argument
	"""
	
	self.id=str(uuid.uuid4())
	self.created_at=datetime.now()
	self.updated_at=datetime.now()
	date_now = "%Y-%m-%dT%H:%M:%S.%f"

	 if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, date_now)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)


def __str__(self):
	""" should print class name Id and dect
	"""
	name_clas = self.__class__.__name__
        return "[{}] ({}) {}".format(name_cls, self.id, self.__dict__)

def save(self):
	""" updates the public instance attribute
	"""
	self.updated_at = datetime.now()
	models.storage.save()


def to_dict(self):
	"""Return Dictionary
	 adds key/value pair __class__ representing
	"""
	bj_dict = self.__dict__.copy()
	bj_dict["__class__"] = self.__class__.__name__
	bj_dict["created_at"] = self.created_at.isoformat()
	bj_dict["updated_at"] = self.updated_at.isoformat()
	return bj_dict	
