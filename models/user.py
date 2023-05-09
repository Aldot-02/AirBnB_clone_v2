#!/usr/bin/python3
""" This is the User Class """
from models.base_model import BaseModel


class User(BaseModel):
    """ A class representing a user, which inherits from the BaseModel class. """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
