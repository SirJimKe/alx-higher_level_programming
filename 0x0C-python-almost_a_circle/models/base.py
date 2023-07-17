#!/usr/bin/python3
"""This module defines class Base"""


class Base:
    """
    Base class to manage the 'id' attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor for the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
