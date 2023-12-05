#!/usr/bin/python3
"""
10-student module

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

    def to_json(self, attrs=None):
        """convert the object to json object

        Returns:
            The JSON object
        """
        attributes = {}
        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
            for key in attrs:
                if self.__dict__.get(key) is not None:
                    attributes.setdefault(key, self.__dict__.get(key))
        else:
            return self.__dict__
        return attributes
