#!/usr/bin/python3


def main(MYSQL_USERNAME, MYSQL_PASSWD, DB_NAME, SEARCH_ITEM):
    conn = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWD,
        db=DB_NAME,
        charset="utf8")
    cur = conn.cursor()

    cur.execute(
        """SELECT cities.name
            FROM cities JOIN states
            ON cities.state_id = states.id
            WHERE states.name=%s
        """, (SEARCH_ITEM,))
    data = cur.fetchall()
    data = [row[0] for row in data]
    print(', '.join(data))

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
