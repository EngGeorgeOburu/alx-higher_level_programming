#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

conn = MySQLdb.connect (
        host ="localhost",
        port=33-6,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
        )
cur = conn.cursor()
query = """
SELECT cities.name
FROM cities 
JOIN states ON cities.state_id = state.id
WHERE states.name = %s
ORDER BY cities.id ASC
"""
try:
    cur.execute(query, (state_name,))
    cities = cur.fetchall()
    print(', '.join(city[0] forcity in cities))
except Exception as e:
    print("Error:", e)

cur.close()
conn.close()
