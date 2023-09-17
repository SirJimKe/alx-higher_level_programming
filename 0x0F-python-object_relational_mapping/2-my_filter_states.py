#!/usr/bin/python3
"""This module lists all states with N as the first letter"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY '{}'""".format(sys.argv[4]))

    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
