from lib.db import Database


class Geometry:

    def __init__(self):
        self.db = Database()

    #Get all wkb data for each postal code
    def get_wkb_geometry(self):
        return "Not implemented yet"