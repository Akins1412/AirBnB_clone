#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
	"""Represent abstracted storage engines.

	Attributes:
		__file_path (str): The name of the file to save the objects to.
		__objects (dict): A dictionary to instantiate object.
	"""
	__file_path = "file.json"
	__objects = {}

	def all(self):
	"""Return  dictionary __objects."""
	return FileStorage.__objects

	def new(self, obj):
	"""Set in __objects 'obj' with 'key' <obj_class_name>.id"""
	cls_name = obj.__class__.__name__
	FileStorage.__objects["{}.{}".format(name_ocls, obj.id)] = obj

	def save(self):
	"""Serialize __objects to the new JSON file __file_path."""
	objdict = FileStorage.__objects
	ob_dict = {obj: objdict[obj].tob_dict() for obj in objdict.keys()}
	with open(FileStorage.__file_path, "w") as f:
		json.dump(ob_dict, f)

	def reload(self):
	"""Deserialize the JSON file __file_path __objects when it appears."""
	try:
		with open(FileStorage.__file_path) as f:
		ob_dict = json.load(f)
		for objs in o_dict.values():
			cls_name = objs["__class__"]
			del objs["__class__"]
			self.new(eval(name_cls)(**objs))
	except FileNotFoundError:
	return
