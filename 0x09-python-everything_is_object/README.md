# Project: 0x09. Python - Everything is object

This directory contains projects focused on understanding the fundamental concepts of objects in Python. The tasks cover topics such as object identity, mutability, aliasing, and how Python handles variables and data structures.

## Resources

### Read or watch

- [9.10. Objects and values](https://docs.python.org/3/reference/datamodel.html#objects-values-and-types)
- [9.11. Aliasing](https://realpython.com/python-variables/)
- [Immutable vs mutable types](https://realpython.com/pointers-in-python/)
- [Mutation](https://realpython.com/python-mutable-vs-immutable/)
- [9.12. Cloning lists](https://www.geeksforgeeks.org/python-cloning-copying-list/)
- [Python tuples: immutable but potentially changing](https://www.geeksforgeeks.org/python-tuples/)

## Learning Objectives

### General

- Why Python programming is awesome
- What is an object
- What is the difference between a class and an object or instance
- What is the difference between immutable object and mutable object
- What is a reference
- What is an assignment
- What is an alias
- How to know if two variables are identical
- How to know if two variables are linked to the same object
- How to display the variable identifier (which is the memory address in the CPython implementation)
- What is mutable and immutable
- What are the built-in mutable types
- What are the built-in immutable types
- How does Python pass variables to functions

## Tasks

| Task                                       | File                                                                                                 | Description                                                                                                 |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 0. Who am I?                               | [0-answer.txt](./0-answer.txt)                                                                       | Write the name of the function that returns the type of an object.                                          |
| 1. Where are you?                          | [1-answer.txt](./1-answer.txt)                                                                       | Write the name of the function that returns the unique identifier of an object.                             |
| 2. Right count                             | [2-answer.txt](./2-answer.txt)                                                                       | Write the name of the function that returns the number of references to an object.                          |
| 3. Right count =                           | [3-answer.txt](./3-answer.txt)                                                                       | Write the name of the function that returns the number of references to an object after assignment.         |
| 4. Right count =                           | [4-answer.txt](./4-answer.txt)                                                                       | Write the name of the function that returns the number of references to an object after another assignment. |
| 5. Right count =+                          | [5-answer.txt](./5-answer.txt)                                                                       | Write the name of the function that returns the number of references to an object after incrementing.       |
| 6. Is equal                                | [6-answer.txt](./6-answer.txt)                                                                       | Write the name of the function that checks if two objects are equal.                                        |
| 7. Is the same                             | [7-answer.txt](./7-answer.txt)                                                                       | Write the name of the function that checks if two objects are the same.                                     |
| 8. Is really equal                         | [8-answer.txt](./8-answer.txt)                                                                       | Write the name of the function that checks if two objects are really equal.                                 |
| 9. Is really the same                      | [9-answer.txt](./9-answer.txt)                                                                       | Write the name of the function that checks if two objects are really the same.                              |
| 10. And with a list, is it equal           | [10-answer.txt](./10-answer.txt)                                                                     | Write the name of the function that checks if two lists are equal.                                          |
| 11. And with a list, is it the same        | [11-answer.txt](./11-answer.txt)                                                                     | Write the name of the function that checks if two lists are the same.                                       |
| 12. And with a list, is it really equal    | [12-answer.txt](./12-answer.txt)                                                                     | Write the name of the function that checks if two lists are really equal.                                   |
| 13. And with a list, is it really the same | [13-answer.txt](./13-answer.txt)                                                                     | Write the name of the function that checks if two lists are really the same.                                |
| 14. List append                            | [14-answer.txt](./14-answer.txt)                                                                     | Write the name of the function that appends an element to a list.                                           |
| 15. List add                               | [15-answer.txt](./15-answer.txt)                                                                     | Write the name of the function that adds an element to a list.                                              |
| 16. Integer incrementation                 | [16-answer.txt](./16-answer.txt)                                                                     | Write the name of the function that increments an integer.                                                  |
| 17. List incrementation                    | [17-answer.txt](./17-answer.txt)                                                                     | Write the name of the function that increments each element in a list.                                      |
| 18. List assignation                       | [18-answer.txt](./18-answer.txt)                                                                     | Write the name of the function that assigns a new list to a variable.                                       |
| 19. Copy a list object                     | [19-copy_list.py](./19-copy_list.py)                                                                 | Write a function that returns a copy of a list.                                                             |
| 20. Tuple or not?                          | [20-answer.txt](./20-answer.txt)                                                                     | Write the name of the function that checks if an object is a tuple.                                         |
| 21. Tuple or not?                          | [21-answer.txt](./21-answer.txt)                                                                     | Write the name of the function that checks if an object is a tuple after assignment.                        |
| 22. Tuple or not?                          | [22-answer.txt](./22-answer.txt)                                                                     | Write the name of the function that checks if an object is a tuple after another assignment.                |
| 23. Tuple or not?                          | [23-answer.txt](./23-answer.txt)                                                                     | Write the name of the function that checks if an object is a tuple after incrementing.                      |
| 24. Who I am?                              | [24-answer.txt](./24-answer.txt)                                                                     | Write the name of the function that returns the type of an object.                                          |
| 25. Tuple or not                           | [25-answer.txt](./25-answer.txt)                                                                     | Write the name of the function that checks if an object is a tuple after appending.                         |
| 26. Empty is not empty                     | [26-answer.txt](./26-answer.txt)                                                                     | Write the name of the function that checks if an empty tuple is not empty.                                  |
| 27. Still the same?                        | [27-answer.txt](./27-answer.txt)                                                                     | Write the name of the function that checks if a tuple is still the same after modification.                 |
| 28. Same or not?                           | [28-answer.txt](./28-answer.txt)                                                                     | Write the name of the function that checks if two tuples are the same.                                      |
| 29. #pythonic                              | [100-magic_string.py](./100-magic_string.py)                                                         | Write a function that returns a string "BestSchool" n times the function is called.                         |
| 30. Low memory cost                        | [101-locked_class.py](./101-locked_class.py)                                                         | Write a class `LockedClass` with no attributes except `first_name`.                                         |
| 31. int 1/3                                | [103-line1.txt](./103-line1.txt), [103-line2.txt](./103-line2.txt)                                   | Write the name of the function that returns the integer division of 1 by 3.                                 |
| 32. int 2/3                                | [104-line1.txt](./104-line1.txt), [104-line2.txt](./104-line2.txt), [104-line3.txt](./104-line3.txt) | Write the name of the function that returns the integer division of 2 by 3.                                 |
| 33. int 3/3                                | [105-line1.txt](./105-line1.txt)                                                                     | Write the name of the function that returns the integer division of 3 by 3.                                 |
| 34. Clear strings                          | [106-line1.txt](./106-line1.txt), [106-line2.txt](./106-line2.txt), [106-line3.txt](./106-line3.txt) | Write the name of the function that clears a string.                                                        |
