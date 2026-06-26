#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
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

    # Ştat adına görə şəhərləri tapmaq üçün JOIN sorğusu qururuq
    query = "SELECT cities.name FROM cities " \
            "JOIN states ON cities.state_id = states.id " \
            "WHERE BINARY states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()

    # Şəhərlərin adlarını bir listə yığırıq
    cities = [row[0] for row in rows]

    # Şəhərləri aralarında ", " olacaq şəkildə birləşdirib ekrana çıxarırıq
    print(", ".join(cities))

    cursor.close()
    db.close()
