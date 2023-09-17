#!/usr/bin/python3

import MySQLdb
import sys


def list_states_with_N(username, password, db_name):
    """
    List all states with names starting with 'N' from the database.

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
        sql_query = (
            "SELECT * "
            "FROM states "
            "WHERE name LIKE 'N%' "
            "ORDER BY id ASC")

        cursor.execute(sql_query)

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
        list_states_with_N(username, password, db_name)
