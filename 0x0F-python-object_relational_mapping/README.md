# Project: 0x0F. Python - Object-relational mapping

This directory contains projects focused on understanding and implementing Object-Relational Mapping (ORM) using Python. The tasks cover concepts such as connecting to a MySQL database from a Python script, performing CRUD operations, and using ORM libraries like SQLAlchemy.

## Resources

### Read or watch

- [Object-relational mappers](https://en.wikipedia.org/wiki/Object-relational_mapping)
- [mysqlclient/MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [MySQLdb tutorial](https://www.tutorialspoint.com/python_data_access/python_mysql_database_access.htm)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/14/tutorial/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Introduction to SQLAlchemy](https://realpython.com/python-sqlalchemy/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [10 common stumbling blocks for SQLAlchemy newbies](https://hakibenita.com/sqlalchemy-explained)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [SQLAlchemy Tutorial](https://overiq.com/sqlalchemy-101/)
- [Python Virtual Environments: A primer](https://realpython.com/python-virtual-environments-a-primer/)

## Learning Objectives

### General

- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to `SELECT` rows in a MySQL table from a Python script
- How to `INSERT` rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to create a Python Virtual Environment

## Tasks

| Task                           | File                                                                                                                                                                       | Description                                                                                                                      |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| 0. Get all states              | [0-select_states.py](./0-select_states.py)                                                                                                                                 | Write a script that lists all `states` from the database `hbtn_0e_0_usa`.                                                        |
| 1. Filter states               | [1-filter_states.py](./1-filter_states.py)                                                                                                                                 | Write a script that lists all `states` with a name starting with `N` from the database `hbtn_0e_0_usa`.                          |
| 2. Filter states by user input | [2-my_filter_states.py](./2-my_filter_states.py)                                                                                                                           | Write a script that takes in an argument and displays all values in the `states` table where `name` matches the argument.        |
| 3. SQL Injection...            | [3-my_safe_filter_states.py](./3-my_safe_filter_states.py)                                                                                                                 | Write a script that takes in an argument and displays all values in the `states` table where `name` matches the argument safely. |
| 4. Cities by states            | [4-cities_by_state.py](./4-cities_by_state.py)                                                                                                                             | Write a script that lists all `cities` from the database `hbtn_0e_4_usa`.                                                        |
| 5. All cities by state         | [5-filter_cities.py](./5-filter_cities.py)                                                                                                                                 | Write a script that takes in the name of a state as an argument and lists all `cities` of that state.                            |
| 6. First state model           | [model_state.py](./model_state.py)                                                                                                                                         | Write a Python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.                 |
| 7. All states via SQLAlchemy   | [7-model_state_fetch_all.py](./7-model_state_fetch_all.py)                                                                                                                 | Write a script that lists all `State` objects from the database `hbtn_0e_6_usa`.                                                 |
| 8. First state                 | [8-model_state_fetch_first.py](./8-model_state_fetch_first.py)                                                                                                             | Write a script that prints the first `State` object from the database `hbtn_0e_6_usa`.                                           |
| 9. Contains `a`                | [9-model_state_filter_a.py](./9-model_state_filter_a.py)                                                                                                                   | Write a script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.                     |
| 10. Get a state                | [10-model_state_my_get.py](./10-model_state_my_get.py)                                                                                                                     | Write a script that prints the `State` object with the `name` passed as argument from the database `hbtn_0e_6_usa`.              |
| 11. Add a new state            | [11-model_state_insert.py](./11-model_state_insert.py)                                                                                                                     | Write a script that adds the `State` object “Louisiana” to the database `hbtn_0e_6_usa`.                                         |
| 12. Update a state             | [12-model_state_update_id_2.py](./12-model_state_update_id_2.py)                                                                                                           | Write a script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.                                      |
| 13. Delete states              | [13-model_state_delete_a.py](./13-model_state_delete_a.py)                                                                                                                 | Write a script that deletes all `State` objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.         |
| 14. Cities in state            | [model_city.py](./model_city.py), [14-model_city_fetch_by_state.py](./14-model_city_fetch_by_state.py)                                                                     | Write a Python file that contains the class definition of a `City` and an instance `Base = declarative_base()`.                  |
| 15. City relationship          | [relationship_city.py](./relationship_city.py), [relationship_state.py](./relationship_state.py), [100-relationship_states_cities.py](./100-relationship_states_cities.py) | Improve the files `model_city.py` and `model_state.py`, and save them as `relationship_city.py` and `relationship_state.py`.     |
| 16. List relationship          | [101-relationship_states_cities_list.py](./101-relationship_states_cities_list.py)                                                                                         | Write a script that lists all `State` objects, and corresponding `City` objects, contained in the database `hbtn_0e_101_usa`.    |
| 17. From city                  | [102-relationship_cities_states_list.py](./102-relationship_cities_states_list.py)                                                                                         | Write a script that lists all `City` objects from the database `hbtn_0e_101_usa`.                                                |
