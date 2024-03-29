#!/usr/bin/python3
"""Retrieving all states from the db using MySQLdb connector
"""


def main(MYSQL_USERNAME, MYSQL_PASSWD, DB_NAME):
    """Retrieve all states from the db

    Arguments:
        MYSQL_USERNAME -- DB username
        MYSQL_PASSWD -- DB password
        DB_NAME -- DB name
    """
    conn = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWD,
        db=DB_NAME,
        charset="utf8")
    cur = conn.cursor()

    cur.execute('SELECT * FROM states ORDER BY states.id ASC')
    data = cur.fetchall()
    for row in data:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    import MySQLdb
    import sys

    MYSQL_USERNAME = sys.argv[1]
    MYSQL_PASSWD = sys.argv[2]
    DB_NAME = sys.argv[3]

    main(MYSQL_USERNAME, MYSQL_PASSWD, DB_NAME)
