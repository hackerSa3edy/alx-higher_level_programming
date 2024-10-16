# Project: 0x0C. Python - Almost a circle

This directory contains projects focused on understanding and implementing various Python concepts such as classes, inheritance, and unit testing. The tasks cover creating and managing classes, serialization/deserialization, and writing unit tests.

## Resources

### Read or watch

- [args/kwargs](https://realpython.com/python-kwargs-and-args/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3/library/unittest.html)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## Learning Objectives

### General

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Tasks

| Task                                                | File                                                                           | Description                                                                                                                                                    |
| --------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0. If it's not tested it doesn't work               | [tests/](./tests/)                                                             | Write unit tests for the classes and methods. _(Not implemented yet)_                                                                                          |
| 1. Base class                                       | [models/base.py](./models/base.py), [models/**init**.py](./models/__init__.py) | Write a class Base with private class attribute `__nb_objects` and a class constructor.                                                                        |
| 2. First Rectangle                                  | [models/rectangle.py](./models/rectangle.py)                                   | Write a class Rectangle that inherits from Base.                                                                                                               |
| 3. Validate attributes                              | [models/rectangle.py](./models/rectangle.py)                                   | Update the class Rectangle by adding validation of all setter methods and instantiation.                                                                       |
| 4. Area first                                       | [models/rectangle.py](./models/rectangle.py)                                   | Update the class Rectangle by adding the public method `def area(self):` that returns the area value of the Rectangle instance.                                |
| 5. Display #0                                       | [models/rectangle.py](./models/rectangle.py)                                   | Update the class Rectangle by adding the public method `def display(self):` that prints in stdout the Rectangle instance with the character `#`.               |
| 6. **str**                                          | [models/rectangle.py](./models/rectangle.py)                                   | Update the class Rectangle by overriding the `__str__` method to return a custom string representation.                                                        |
| 7. Display #1                                       | [models/rectangle.py](./models/rectangle.py)                                   | Update the class Rectangle by enhancing the `def display(self):` method to handle `x` and `y` coordinates.                                                     |
| 8. Update #0                                        | [models/rectangle.py](./models/rectangle.py)                                   | Update the class Rectangle by adding the public method `def update(self, *args):` that assigns an argument to each attribute.                                  |
| 9. Update #1                                        | [models/rectangle.py](./models/rectangle.py)                                   | Update the class Rectangle by updating the public method `def update(self, *args, **kwargs):` to assign a key/value argument to attributes.                    |
| 10. And now, the Square!                            | [models/square.py](./models/square.py)                                         | Write a class Square that inherits from Rectangle.                                                                                                             |
| 11. Square size                                     | [models/square.py](./models/square.py)                                         | Update the class Square by adding the public getter and setter `size`.                                                                                         |
| 12. Square update                                   | [models/square.py](./models/square.py)                                         | Update the class Square by adding the public method `def update(self, *args, **kwargs):` that assigns attributes.                                              |
| 13. Rectangle instance to dictionary representation | [models/rectangle.py](./models/rectangle.py)                                   | Update the class Rectangle by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a Rectangle.                   |
| 14. Square instance to dictionary representation    | [models/square.py](./models/square.py)                                         | Update the class Square by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a Square.                         |
| 15. Dictionary to JSON string                       | [models/base.py](./models/base.py)                                             | Update the class Base by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`. |
| 16. JSON string to file                             | [models/base.py](./models/base.py)                                             | Update the class Base by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file.      |
| 17. JSON string to dictionary                       | [models/base.py](./models/base.py)                                             | Update the class Base by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`.  |
| 18. Dictionary to Instance                          | [models/base.py](./models/base.py)                                             | Update the class Base by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set.                    |
| 19. File to instances                               | [models/base.py](./models/base.py)                                             | Update the class Base by adding the class method `def load_from_file(cls):` that returns a list of instances.                                                  |
| 20. JSON ok, but CSV?                               | [models/](./models/)                                                           | Update the class Base by adding methods to handle CSV serialization and deserialization.                                                                       |
| 21. Let's draw it                                   | [models/base.py](./models/base.py)                                             | Update the class Base by adding a static method `def draw(list_rectangles, list_squares):` that opens a window and draws all the Rectangles and Squares.       |
