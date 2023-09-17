#!/usr/bin/python3
"""A module that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    List all states from the database.

    :param username: MySQL username.
    :param password: MySQL password.
    :param database_name: Name of the database to connect to.
    """
    connection = None

    try:
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=db_name)

        cursor = connection.cursor()

        cursor.execute('SELECT * FROM states ORDER BY id ASC')

        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Check args")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_states(username, password, db_name)
