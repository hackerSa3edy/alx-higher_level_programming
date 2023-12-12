#!/usr/bin/python3
"""Module base"""
import json
import csv


class Base():
    """Defines a base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assign the public instance attribute id
        Args:
            id(int): integer value to manage id in this project
        Return:
            Always nothing.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns the JSON
            string representation
        Args:
            list_dictionaries(dict): List of dictionaries
        Return:
            JSON string
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Method that writes the JSON string representation
            of list_objs to a file
        Args:
            list_objs(list): List of objects
        Return:
            Always nothing
        """
        obj_list = []
        if list_objs:
            for obj in list_objs:
                json_dict = obj.to_dictionary()
                obj_list.append(json_dict)
        json_str = cls.to_json_string(obj_list)
        with open(f"{cls.__name__}.json", 'w') as json_file:
            json_file.write(json_str)

    @classmethod
    def save_to_file_csv(cls, dict_list):
        """Method that serializes in CSV
        Args:
            list_objs(list): List of objects
        Return:
            Always nothing
        """
        obj_list = []
        for instance in dict_list:
            obj_list.append(instance.to_dictionary())
        with open(f"{cls.__name__}.csv", 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=obj_list[0].keys())
            writer.writeheader()
            writer.writerows(obj_list)

    @staticmethod
    def from_json_string(json_string):
        """Method that returns the list of the
            JSON string representation
        Args:
            json_string: JSON string
        Return:
            Python object
        """
        if json_string is None or json_string == '':
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update the class Base and returns a instance with all
            attributes already set
        Args:
            dictionary: Dictionary with all attributes of the object
        Return:
            A instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 3)
        elif cls.__name__ == 'Square':
            dummy = cls(2, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Method that returns a list of instances
            - the type of these instances depends on cls
        """
        l_instances = []
        try:
            with open(f"{cls.__name__}.json", 'r') as r_instances:
                json_des = cls.from_json_string(r_instances.read())

        except FileNotFoundError:
            return []

        for obj in json_des:
            l_instances.append(cls.create(**obj))

        return l_instances

    @classmethod
    def load_from_file_csv(cls):
        """Method that deserializes in CSV
        """
        obj_list = []
        try:
            with open(f"{cls.__name__}.csv") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    obj_list.append(instance)
        except FileNotFoundError:
            return obj_list
        return obj_list
