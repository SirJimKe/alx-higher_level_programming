#!/usr/bin/python3
"""a class Student that defines a student"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the serialized
            attributes of the Student instance.
        """
        if attrs is None:
            attrs = vars(self).keys()
        description = {}
        for attr in attrs:
            if hasattr(self, attr):
                value = getattr(self, attr)
                if isinstance(value, (list, dict, str, int, bool)):
                    description[attr] = value
        return description

    def reload_from_json(self, json):
        for attr, value in json.items():
            setattr(self, attr, value)
