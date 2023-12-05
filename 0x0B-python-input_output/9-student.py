#!/usr/bin/python3
"""
9-student module

Initiates Student class that defines a student
"""


class Student():
    """Student class
    """
    def __init__(self, first_name, last_name, age):
        """Initialize instance attributes

        Arguments:
            first_name -- Student's first name
            last_name -- Student's Last name
            age -- Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """convert the object to json object

        Returns:
            The JSON object
        """
        return self.__dict__
