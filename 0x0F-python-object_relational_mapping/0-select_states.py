#!/usr/bin/pyhton3

"""A script that lists all states from the database hbtn_0e_0_usa:

Arguments: mysql username, mysql password and database name.

"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=hbtn_0e_0_usa)

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
