#!/usr/bin/python3
""" This is the City class. """
from models.base_model import BaseModel


class City(BaseModel):
    """ Subclass of BaseModel for city objects. """
    state_id = ""
    name = ""
