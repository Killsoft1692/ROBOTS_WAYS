import os

from settings import MAPS_FOLDER


class Uploader:
    """
    File uploader
    """
    def __init__(self, db, mapper):
        self.db = db
        self.map = mapper

    def upload(self, filename):
        with open(os.path.join(MAPS_FOLDER, filename), 'r') as file:
            data = file.readlines()
            if self.map.is_valid(data):
                # Saving to db
                self.db.ways.insert({'map': {'data': self.map.interpret(data), 'source': filename}})
            else:
                raise ValueError('This file isn\'t compatible with this program')
