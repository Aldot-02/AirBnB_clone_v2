#!/usr/bin/python3
""" Definition of a Class called BaseModel """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """ Constructor for the BaseModel class. """

    def __init__(self, *args, **kwargs):
        """ Construct a new BaseModel object. """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """ Return a string representation of the BaseModel object. """
        return('[' + type(self).__name__ + '] (' + str(self.id) +
               ') ' + str(self.__dict__))

    def save(self):
        """ Save the BaseModel object. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Return a dictionary representing the BaseModel object. """
        aux_dict = self.__dict__.copy()
        aux_dict['__class__'] = self.__class__.__name__
        aux_dict['created_at'] = self.created_at.isoformat()
        aux_dict['updated_at'] = self.updated_at.isoformat()
        return aux_dict
