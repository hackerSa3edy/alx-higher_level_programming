# Project: 0x07. Python - Test-driven development

This directory contains projects focused on understanding and implementing test-driven development (TDD) in Python. The tasks cover writing tests using `doctest` and `unittest` modules, creating documentation, and ensuring code correctness through testing.

## Resources

### Read or watch

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [doctest – Testing through documentation](https://realpython.com/python-doctest/)
- [Unit Tests in Python](https://realpython.com/python-testing/)
- [Unittest module](https://docs.python.org/3/library/unittest.html)
- [Interactive and Non-interactive tests](https://www.geeksforgeeks.org/interactive-vs-non-interactive-mode-python/)

## Learning Objectives

### General

- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Tasks

| Task                          | File                                                                                                                 | Description                                                                                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 0. Integers addition          | [0-add_integer.py](./0-add_integer.py), [tests/0-add_integer.txt](./tests/0-add_integer.txt)                         | Write a function that adds 2 integers and includes tests using `doctest`.                                                              |
| 1. Divide a matrix            | [2-matrix_divided.py](./2-matrix_divided.py), [tests/2-matrix_divided.txt](./tests/2-matrix_divided.txt)             | Write a function that divides all elements of a matrix and includes tests using `doctest`.                                             |
| 2. Say my name                | [3-say_my_name.py](./3-say_my_name.py), [tests/3-say_my_name.txt](./tests/3-say_my_name.txt)                         | Write a function that prints "My name is `<first name>` `<last name>`" and includes tests using `doctest`.                             |
| 3. Print square               | [4-print_square.py](./4-print_square.py), [tests/4-print_square.txt](./tests/4-print_square.txt)                     | Write a function that prints a square with the character `#` and includes tests using `doctest`.                                       |
| 4. Text indentation           | [5-text_indentation.py](./5-text_indentation.py), [tests/5-text_indentation.txt](./tests/5-text_indentation.txt)     | Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, `:` and includes tests using `doctest`. |
| 5. Max integer - Unittest     | [tests/6-max_integer_test.py](./tests/6-max_integer_test.py)                                                         | Write unittests for a function that finds the max integer in a list.                                                                   |
| 6. Matrix multiplication      | [100-matrix_mul.py](./100-matrix_mul.py), [tests/100-matrix_mul.txt](./tests/100-matrix_mul.txt)                     | Write a function that multiplies 2 matrices and includes tests using `doctest`.                                                        |
| 7. Lazy matrix multiplication | [101-lazy_matrix_mul.py](./101-lazy_matrix_mul.py), [tests/101-lazy_matrix_mul.txt](./tests/101-lazy_matrix_mul.txt) | Write a function that multiplies 2 matrices using NumPy and includes tests using `doctest`.                                            |
| 8. CPython #3: Python Strings | [102-python.c](./102-python.c)                                                                                       | Create a C function that prints some basic info about Python strings.                                                                  |
