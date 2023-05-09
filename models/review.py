#!/usr/bin/python3
""" This is a class for handling reviews. """
from models.base_model import BaseModel


class Review(BaseModel):
    """ This class extends the BaseModel to include additional attributes for handling reviews. """
    place_id = ""
    user_id = ""
    text = ""
