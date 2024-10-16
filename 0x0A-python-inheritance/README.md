# Project: 0x0A. Python - Inheritance

This directory contains projects focused on understanding and implementing inheritance in Python. The tasks cover concepts such as creating subclasses, overriding methods, and using built-in functions related to inheritance.

## Resources

### Read or watch

- [Inheritance](https://realpython.com/inheritance-composition-python/)
- [Multiple inheritance](https://www.python-course.eu/python3_multiple_inheritance.php)
- [Inheritance in Python](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Learn to Program 10 : Inheritance Magic Methods](https://www.youtube.com/watch?v=RSl87lqOXDE)

## Learning Objectives

### General

- Why Python programming is awesome
- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## Tasks

| Task                          | File                                                                                                 | Description                                                                                                                                              |
| ----------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0. Lookup                     | [0-lookup.py](./0-lookup.py)                                                                         | Write a function that returns the list of available attributes and methods of an object.                                                                 |
| 1. My list                    | [1-my_list.py](./1-my_list.py), [tests/1-my_list.txt](./tests/1-my_list.txt)                         | Write a class MyList that inherits from list.                                                                                                            |
| 2. Exact same object          | [2-is_same_class.py](./2-is_same_class.py)                                                           | Write a function that returns True if the object is exactly an instance of the specified class.                                                          |
| 3. Same class or inherit from | [3-is_kind_of_class.py](./3-is_kind_of_class.py)                                                     | Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class. |
| 4. Only sub class of          | [4-inherits_from.py](./4-inherits_from.py)                                                           | Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class.             |
| 5. Geometry module            | [5-base_geometry.py](./5-base_geometry.py)                                                           | Write an empty class BaseGeometry.                                                                                                                       |
| 6. Improve Geometry           | [6-base_geometry.py](./6-base_geometry.py)                                                           | Write a class BaseGeometry with a public instance method `def area(self):` that raises an Exception with the message `area() is not implemented`.        |
| 7. Integer validator          | [7-base_geometry.py](./7-base_geometry.py), [tests/7-base_geometry.txt](./tests/7-base_geometry.txt) | Write a class BaseGeometry with a public instance method `def integer_validator(self, name, value):` that validates `value`.                             |
| 8. Rectangle                  | [8-rectangle.py](./8-rectangle.py)                                                                   | Write a class Rectangle that inherits from BaseGeometry.                                                                                                 |
| 9. Full rectangle             | [9-rectangle.py](./9-rectangle.py)                                                                   | Write a class Rectangle that inherits from BaseGeometry (based on 8-rectangle.py).                                                                       |
| 10. Square #1                 | [10-square.py](./10-square.py)                                                                       | Write a class Square that inherits from Rectangle (9-rectangle.py).                                                                                      |
| 11. Square #2                 | [11-square.py](./11-square.py)                                                                       | Write a class Square that inherits from Rectangle (10-square.py).                                                                                        |
| 12. My integer                | [100-my_int.py](./100-my_int.py)                                                                     | Write a class MyInt that inherits from int.                                                                                                              |
| 13. Can I?                    | [101-add_attribute.py](./101-add_attribute.py)                                                       | Write a function that adds a new attribute to an object if it’s possible.                                                                                |
