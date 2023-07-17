#!/usr/bin/python3
"""This module defines class Base"""

import json
import csv
from io import StringIO


class Base:
    """
    Base class to manage the 'id' attribute and provide\
    serialization/deserialization functionality.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor for the Base class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(data):
        """
        Returns the JSON string representation of the given data.
        """
        if data is None or len(data) == 0:
            return "[]"
        return json.dumps(data)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of the list_objs to a file.
        """
        filename = f"{cls.__name__}.json"
        data = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to_json_string(data)
        with open(filename, 'w') as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of dictionaries represented by the given JSON string.
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **kwargs):
        """
        Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()
        dummy.update(**kwargs)
        return dummy

    def update(self, *args, **kwargs):
        """
        Assigns attributes based on positional and keyword arguments.
        """
        attributes = ["id", "width", "height", "x", "y"]
        for i, arg in enumerate(args):
            setattr(self, attributes[i], arg)
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a JSON file.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                data = cls.from_json_string(json_str)
                return [cls.create(**item) for item in data]
        except FileNotFoundError:
            return []

    @staticmethod
    def to_csv_string(list_instances):
        """
        Returns the CSV string representation of the given list of instances.
        """
        if list_instances is None or len(list_instances) == 0:
            return ""
        first_instance = list_instances[0]
        fieldnames = list(first_instance.__dict__.keys())
        csv_str = ""
        with StringIO() as output:
            writer = csv.DictWriter(output, fieldnames=fieldnames)
            writer.writeheader()
            for instance in list_instances:
                writer.writerow(instance.__dict__)
            csv_str = output.getvalue()
        return csv_str

    @staticmethod
    def from_csv_string(csv_string):
        """
        Returns the list of instances represented by the given CSV string.
        """
        if csv_string is None or csv_string == "":
            return []
        list_instances = []
        with StringIO(csv_string) as input_data:
            reader = csv.DictReader(input_data)
            for row in reader:
                instance = cls.create(**row)
                list_instances.append(instance)
        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes and saves instances to a CSV file.
        """
        filename = f"{cls.__name__}.csv"
        csv_str = cls.to_csv_string(list_objs)
        with open(filename, 'w') as file:
            file.write(csv_str)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes and loads instances from a CSV file.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r') as file:
                csv_str = file.read()
                return cls.from_csv_string(csv_str)
        except FileNotFoundError:
            return []
