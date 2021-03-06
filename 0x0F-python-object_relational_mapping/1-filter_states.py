#!/usr/bin/python3
"""List all states with a name starting with upper N."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Connect to a MySQL server."""
    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states\
    WHERE name REGEXP '^N' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        if ("N" in state[1]):
            print(state)
    cursor.close()
    db.close()
