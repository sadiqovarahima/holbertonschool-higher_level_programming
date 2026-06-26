#!/usr/bin/python3
"""
Script that lists all states with a given name
safe from MySQL injections
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Sətir uzunluğu limitini (79) keçməmək üçün sorğunu iki yerə bölürük
    query = "SELECT * FROM states WHERE BINARY name = %s "\
            "ORDER BY states.id ASC"
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
