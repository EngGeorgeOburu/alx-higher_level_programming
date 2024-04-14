#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb (
            host = "localhost",
            port = 3306,
            user = sys.argv[1],
            passwd = sys.argv[2],
            db = sys.argv[3],
            charset = "utf8"
            )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cur.execute(query, ('%' + sys.argv[4] + '%', ))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()
