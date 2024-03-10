#!/usr/bin/python3
"""This! module stores instances from the Baseclass"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """the class to store instances from Baseclass
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ Returns  dict. __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets the `obj` with the `key` in `__objects`.
        """
        cls_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cls_name, obj.id)] = obj

    def save(self):
        """ Serialize `__objects` to file in  JSON
        """
        objdict = FileStorage.__objects
        o_dict = {obj: objdict[obj].to_dict() for ob in objdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(o_dict, f)

    def reload(self):
        """ If the JSON file exists, deserializes the file to `__objects`
        """
        try:
             with open(FileStorage.__file_path) as f:
                o_jdict = json.load(f)
                for ob in o_dict.values():
                    cls_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(name_cls)(**ob))
        except FileNotFoundError:
            pass
