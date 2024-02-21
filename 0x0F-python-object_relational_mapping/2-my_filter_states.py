#!/usr/bin/python3
"""Retrieving all states which its name matches the specified
item from the db using MySQLdb connector
"""


def main(MYSQL_USERNAME, MYSQL_PASSWD, DB_NAME, SEARCH_ITEM):
    """Retrieving all states which its name matches the specified
    item from the db

    Arguments:
        MYSQL_USERNAME -- DB username
        MYSQL_PASSWD -- DB password
        DB_NAME -- DB name
        SEARCH_ITEM -- Speicified item
    """
    conn = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWD,
        db=DB_NAME,
        charset="utf8")
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name='{:s}'".format(SEARCH_ITEM))
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
    SEARCH_ITEM = sys.argv[4]

    main(MYSQL_USERNAME, MYSQL_PASSWD, DB_NAME, SEARCH_ITEM)
