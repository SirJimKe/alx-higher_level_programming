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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary containing the serialized attributes of the Student instance.
        """
        description = {}
        for attr, value in vars(self).items():
            if isinstance(value, (list, dict, str, int, bool)):
                description[attr] = value
        return description
