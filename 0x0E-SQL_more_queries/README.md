# Project: 0x0E. SQL - More queries

This directory contains projects focused on advanced SQL queries and database management. The tasks cover concepts such as creating users, managing privileges, using constraints, and performing complex queries involving joins, unions, and subqueries.

## Resources

### Read or watch

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL constraints](https://www.mysqltutorial.org/mysql-constraints.aspx)
- [SQL technique: subqueries](https://www.w3schools.com/sql/sql_subqueries.asp)
- [Basic query operation: the join](https://www.w3schools.com/sql/sql_join.asp)
- [SQL technique: multiple joins and the distinct keyword](https://www.sqlshack.com/sql-join-multiple-tables/)
- [SQL technique: join types](https://www.geeksforgeeks.org/sql-join-set-1-inner-left-right-and-full-joins/)
- [SQL technique: union and minus](https://www.w3schools.com/sql/sql_union.asp)
- [MySQL Cheat Sheet](https://www.mysqltutorial.org/mysql-cheat-sheet.aspx)
- [The Seven Types of SQL Joins](https://www.essentialsql.com/the-seven-types-of-sql-joins/)
- [MySQL Tutorial](https://www.mysqltutorial.org/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

## Learning Objectives

### General

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a `PRIMARY KEY`
- What’s a `FOREIGN KEY`
- How to use `NOT NULL` and `UNIQUE` constraints
- How to retrieve data from multiple tables in one request
- What are subqueries
- What are `JOIN` and `UNION`

## Tasks

| Task                         | File                                                                         | Description                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| 0. My privileges!            | [0-privileges.sql](./0-privileges.sql)                                       | Write a script that lists all privileges of the MySQL users.                                      |
| 1. Root user                 | [1-create_user.sql](./1-create_user.sql)                                     | Write a script that creates a new MySQL user.                                                     |
| 2. Read user                 | [2-create_read_user.sql](./2-create_read_user.sql)                           | Write a script that creates a new MySQL user with read-only access to a database.                 |
| 3. Always a name             | [3-force_name.sql](./3-force_name.sql)                                       | Write a script that creates a table with a `NOT NULL` constraint on a column.                     |
| 4. ID can't be null          | [4-never_empty.sql](./4-never_empty.sql)                                     | Write a script that creates a table with a `NOT NULL` constraint on the `id` column.              |
| 5. Unique ID                 | [5-unique_id.sql](./5-unique_id.sql)                                         | Write a script that creates a table with a `UNIQUE` constraint on the `id` column.                |
| 6. States table              | [6-states.sql](./6-states.sql)                                               | Write a script that creates a `states` table.                                                     |
| 7. Cities table              | [7-cities.sql](./7-cities.sql)                                               | Write a script that creates a `cities` table with a `FOREIGN KEY` referencing the `states` table. |
| 8. Cities of California      | [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql) | Write a script that lists all cities of California using a subquery.                              |
| 9. Cities by States          | [9-cities_by_state_join.sql](./9-cities_by_state_join.sql)                   | Write a script that lists all cities by states using a join.                                      |
| 10. Genre ID by show         | [10-genre_id_by_show.sql](./10-genre_id_by_show.sql)                         | Write a script that lists the genre ID for each show.                                             |
| 11. Genre ID for all shows   | [11-genre_id_all_shows.sql](./11-genre_id_all_shows.sql)                     | Write a script that lists the genre ID for all shows.                                             |
| 12. No genre                 | [12-no_genre.sql](./12-no_genre.sql)                                         | Write a script that lists all shows without a genre.                                              |
| 13. Number of shows by genre | [13-count_shows_by_genre.sql](./13-count_shows_by_genre.sql)                 | Write a script that counts the number of shows by genre.                                          |
| 14. My genres                | [14-my_genres.sql](./14-my_genres.sql)                                       | Write a script that lists all genres of shows that belong to a specific user.                     |
| 15. Only Comedy              | [15-comedy_only.sql](./15-comedy_only.sql)                                   | Write a script that lists all comedy shows.                                                       |
| 16. List shows and genres    | [16-shows_by_genre.sql](./16-shows_by_genre.sql)                             | Write a script that lists all shows and their genres.                                             |
