#!/usr/bin/python3
"""Module for class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class square represents a basic square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representtion of Rectangle instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                       self.width)
