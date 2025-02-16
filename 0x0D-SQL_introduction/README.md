# Project: 0x0D. SQL - Introduction

This directory contains projects focused on understanding and implementing basic SQL operations. The tasks cover concepts such as creating databases, tables, and performing various SQL queries.

## Resources

### Read or watch

- [What is Database & SQL?](https://www.youtube.com/watch?v=FR4QIeZaPeM)
- [A Basic MySQL Tutorial](https://www.digitalocean.com/community/tutorials/a-basic-mysql-tutorial)
- [Basic SQL statements: DDL and DML](https://www.geeksforgeeks.org/sql-ddl-dql-dml-dcl-tcl-commands/)
- [Basic queries: SQL and RA](https://www.w3schools.com/sql/sql_select.asp)
- [SQL technique: functions](https://www.w3schools.com/sql/sql_functions.asp)
- [SQL technique: subqueries](https://www.w3schools.com/sql/sql_subqueries.asp)
- [What makes the big difference between a backtick and an apostrophe?](https://stackoverflow.com/questions/11321491/when-to-use-single-quotes-double-quotes-and-backticks-in-mysql)
- [MySQL Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [Installing MySQL on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04)

## Learning Objectives

### General

- What’s a database
- What’s a relational database
- What does SQL stand for
- What’s MySQL
- How to create a database in MySQL
- What does `DDL` and `DML` stand for
- How to `CREATE` or `ALTER` a table
- How to `SELECT` data from a table
- How to `INSERT`, `UPDATE` or `DELETE` data
- What are `subqueries`
- How to use MySQL functions

## Tasks

| Task                 | File                                                                   | Description                                                                                                                         |
| -------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 0. List databases    | [0-list_databases.sql](./0-list_databases.sql)                         | Write a script that lists all databases of your MySQL server.                                                                       |
| 1. Create a database | [1-create_database_if_missing.sql](./1-create_database_if_missing.sql) | Write a script that creates the database `hbtn_0c_0` in your MySQL server.                                                          |
| 2. Delete a database | [2-remove_database.sql](./2-remove_database.sql)                       | Write a script that deletes the database `hbtn_0c_0` in your MySQL server.                                                          |
| 3. List tables       | [3-list_tables.sql](./3-list_tables.sql)                               | Write a script that lists all the tables of a database in your MySQL server.                                                        |
| 4. First table       | [4-first_table.sql](./4-first_table.sql)                               | Write a script that creates a table called `first_table` in the current database in your MySQL server.                              |
| 5. Full description  | [5-full_table.sql](./5-full_table.sql)                                 | Write a script that prints the full description of the table `first_table` from the database in your MySQL server.                  |
| 6. List all in table | [6-list_values.sql](./6-list_values.sql)                               | Write a script that lists all rows of the table `first_table` from the database in your MySQL server.                               |
| 7. First add         | [7-insert_value.sql](./7-insert_value.sql)                             | Write a script that inserts a new row in the table `first_table` in your MySQL server.                                              |
| 8. Count 89          | [8-count_89.sql](./8-count_89.sql)                                     | Write a script that displays the number of records with `id = 89` in the table `first_table` of your MySQL server.                  |
| 9. Full creation     | [9-full_creation.sql](./9-full_creation.sql)                           | Write a script that creates a table `second_table` and adds multiple rows.                                                          |
| 10. List by best     | [10-top_score.sql](./10-top_score.sql)                                 | Write a script that lists all records of the table `second_table` in your MySQL server in descending order by `score`.              |
| 11. Select the best  | [11-best_score.sql](./11-best_score.sql)                               | Write a script that lists all records with a `score >= 10` in the table `second_table` in your MySQL server.                        |
| 12. Cheating is bad  | [12-no_cheating.sql](./12-no_cheating.sql)                             | Write a script that updates the score of Bob to `10` in the table `second_table`.                                                   |
| 13. Score too low    | [13-change_class.sql](./13-change_class.sql)                           | Write a script that removes all records with a `score <= 5` in the table `second_table`.                                            |
| 14. Average          | [14-average.sql](./14-average.sql)                                     | Write a script that computes the average score of all records in the table `second_table`.                                          |
| 15. Number by score  | [15-groups.sql](./15-groups.sql)                                       | Write a script that lists the number of records with the same score in the table `second_table`.                                    |
| 16. Say my name      | [16-no_link.sql](./16-no_link.sql)                                     | Write a script that lists all records of the table `second_table` and displays only the `id` and `name`.                            |
| 17. Go to UTF8       | [100-move_to_utf8.sql](./100-move_to_utf8.sql)                         | Write a script that converts `second_table` to UTF8.                                                                                |
| 18. Temperatures #0  | [101-avg_temperatures.sql](./101-avg_temperatures.sql)                 | Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature in descending order.               |
| 19. Temperatures #1  | [102-top_city.sql](./102-top_city.sql)                                 | Write a script that displays the top 3 cities with the highest temperature (Fahrenheit) ordered by temperature in descending order. |
| 20. Temperatures #2  | [103-max_state.sql](./103-max_state.sql)                               | Write a script that displays the max temperature of each state (ordered by State name).                                             |
