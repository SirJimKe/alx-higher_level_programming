#!/usr/bin/python3
"""This module lists all cities from the database"""

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
    state_name = sys.argv[4]

    sql_query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC")

    cur.execute(sql_query, (state_name,))

    cities = cur.fetchall()
    print(", ".join(city[0] for city in cities))

    cur.close()
    db.close()
