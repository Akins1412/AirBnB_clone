#!/usr/bin/python3
"""This! module stores instances from the Baseclass"""

from datetime import datetime
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
        cls_name = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[cls_name] = obj

    def save(self):
        """ Serialize `__objects` to file in  JSON
        """
        serialized_objects = {}
        for ke, value in FileStorage.__objects.items():
            serialized_objects[ky] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """ If the JSON file exists, deserializes the file to `__objects`
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, val in data.items():

                    # Remove from the dictionary
                    del val["__class__"]

                    # Ensure conversion to datetime object
                    form = "%Y-%m-%dT%H:%M:%S.%f"
                    cl = "updated_at"  # Attribute to match
                    if cl in val:
                        val[cl] = datetime.strptime(value[cl], form)

                    cls_name, obj_id = key.split('.')
                    obj_instance = eval(class_name)(**value)
		FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
