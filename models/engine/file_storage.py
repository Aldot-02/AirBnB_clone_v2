#!/usr/bin/python3
""" This is the FileStorage class that serializes instances to a JSON file
and deserializes a JSON file to instances. """
import json
import uuid
import os
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This class contains methods to handle serialization and deserialization
    of instances to and from a JSON file. """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns a dictionary of objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets an object in the dictionary with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ Serializes objects to a JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, fname)

    def reload(self):
        """ Reloads the file """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, val in l_json.items():
                    FileStorage.__objects[key] = eval(
                        val['__class__'])(**val)
