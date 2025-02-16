# Project: 0x0B. Python - Input/Output

This directory contains projects focused on understanding and implementing file input and output operations in Python. The tasks cover concepts such as reading and writing files, working with JSON, and serialization/deserialization.

## Resources

### Read or watch

- [7.2. Reading and Writing Files](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [8.7. Predefined Clean-up Actions](https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions)
- [Dive Into Python 3: Chapter 11. Files](https://diveintopython3.problemsolving.io/files.html)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [Learn to Program 8 : Reading / Writing Files](https://www.youtube.com/watch?v=EukxMIsNeqU)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/chapter8/)
- [All about py-file I/O](https://realpython.com/read-write-files-python/)

## Learning Objectives

### General

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is `JSON`
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Tasks

| Task                              | File                                                   | Description                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0. Read file                      | [0-read_file.py](./0-read_file.py)                     | Write a function that reads a text file (UTF8) and prints it to stdout.                                                                                                  |
| 1. Write to a file                | [1-write_file.py](./1-write_file.py)                   | Write a function that writes a string to a text file (UTF8) and returns the number of characters written.                                                                |
| 2. Append to a file               | [2-append_write.py](./2-append_write.py)               | Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added.                                                      |
| 3. To JSON string                 | [3-to_json_string.py](./3-to_json_string.py)           | Write a function that returns the JSON representation of an object (string).                                                                                             |
| 4. From JSON string to Object     | [4-from_json_string.py](./4-from_json_string.py)       | Write a function that returns an object (Python data structure) represented by a JSON string.                                                                            |
| 5. Save Object to a file          | [5-save_to_json_file.py](./5-save_to_json_file.py)     | Write a function that writes an Object to a text file, using a JSON representation.                                                                                      |
| 6. Create object from a JSON file | [6-load_from_json_file.py](./6-load_from_json_file.py) | Write a function that creates an Object from a “JSON file”.                                                                                                              |
| 7. Load, add, save                | [7-add_item.py](./7-add_item.py)                       | Write a script that adds all arguments to a Python list, and then save them to a file.                                                                                   |
| 8. Class to JSON                  | [8-class_to_json.py](./8-class_to_json.py)             | Write a function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object. |
| 9. Student to JSON                | [9-student.py](./9-student.py)                         | Write a class Student that defines a student by first_name, last_name, and age.                                                                                          |
| 10. Student to JSON with filter   | [10-student.py](./10-student.py)                       | Write a class Student that defines a student by first_name, last_name, and age with a method to retrieve a dictionary representation with filter.                        |
| 11. Student to disk and reload    | [11-student.py](./11-student.py)                       | Write a class Student that defines a student by first_name, last_name, and age with methods to reload from a dictionary.                                                 |
| 12. Pascal's Triangle             | [12-pascal_triangle.py](./12-pascal_triangle.py)       | Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n.                                              |
| 13. Search and update             | [100-append_after.py](./100-append_after.py)           | Write a function that inserts a line of text to a file, after each line containing a specific string.                                                                    |
| 14. Log parsing                   | [101-stats.py](./101-stats.py)                         | Write a script that reads stdin line by line and computes metrics.                                                                                                       |
