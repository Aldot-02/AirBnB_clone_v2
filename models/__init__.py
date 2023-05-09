#!/usr/bin/python3

""" This script initializes the FileStorage class and creates a storage object
for storing data in a file. The object is then reloaded to ensure any stored data is
retrieved and ready for use. """

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
