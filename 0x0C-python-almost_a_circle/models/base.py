#!/usr/bin/python3
"""This module defines class Base"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        jstr = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        with open(filename, 'w') as file:
            file.write(jstr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**dictionary)
        return dummy

    def update(self, *args, **kwargs):
        """Assigns attributes based on positional and keyword arguments."""
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a JSON file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                list_dicts = cls.from_json_string(json_str)
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def to_csv_string(list_instances):
        """Returns the CSV string representation of list_instances."""
        if list_instances is None or len(list_instances) == 0:
            return ""
        if type(list_instances[0]) == Rectangle:
            fieldnames = ['id', 'width', 'height', 'x', 'y']
        elif type(list_instances[0]) == Square:
            fieldnames = ['id', 'size', 'x', 'y']
        else:
            raise TypeError("Unsupported class type")
        csv_str = ""
        csv_writer = csv.DictWriter(csv_str, fieldnames=fieldnames)
        csv_writer.writeheader()
        for instance in list_instances:
            csv_writer.writerow(instance.to_dictionary())
        return csv_str

    @staticmethod
    def from_csv_string(csv_string):
        """Returns the list of instances represented by csv_string."""
        if csv_string is None or csv_string == "":
            return []
        csv_reader = csv.DictReader(csv_string.splitlines())
        list_instances = []
        for row in csv_reader:
            if 'width' in row:  # Rectangle
                instance = Rectangle(0, 0)
                instance.update(**row)
            elif 'size' in row:  # Square
                instance = Square(0)
                instance.update(**row)
            else:
                raise ValueError("Invalid CSV format")
            list_instances.append(instance)
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes and saves instances to a CSV file."""
        filename = cls.__name__ + ".csv"
        csv_str = cls.to_csv_string(list_objs)
        with open(filename, 'w') as file:
            file.write(csv_str)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes and loads instances from a CSV file."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                csv_str = file.read()
                return cls.from_csv_string(csv_str)
        except FileNotFoundError:
            return []
