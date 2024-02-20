#!/usr/bin/python3


def main(MYSQL_USERNAME, MYSQL_PASSWD, DB_NAME):
    conn = MySQLdb.Connect(
        host="localhost",
        port=3306,
        user=MYSQL_USERNAME,
        passwd=MYSQL_PASSWD,
        db=DB_NAME,
        charset="utf8")
    cur = conn.cursor()

    cur.execute(
        """SELECT cities.id,
                cities.name,
                states.name
            FROM cities JOIN states
            ON states.id = cities.state_id
            ORDER BY cities.id ASC
            """)
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
