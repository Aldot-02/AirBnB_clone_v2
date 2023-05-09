#!/usr/bin/python3
""" Running tests on Amenity """
import unittest
import pep8
from models.amenity import Amenity

class Amenity_testing(unittest.TestCase):
    """ This is for checking BaseModel """

    def testpep8(self):
        """ testing or experimenting the codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/amenity.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Detected style issues and potential problems in the code.")
