#!/usr/bin/python3

"""
A script listing all states from the database
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    """
    Acessing database and getting
    states from the database
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset='utf8')

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
