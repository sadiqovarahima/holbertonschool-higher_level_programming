#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Verilənlər bazasına qoşulma (Port mütləq 3306 olmalıdır)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    
    cursor = db.cursor()
    
    # Şərtdə tələb olunan .format() metodundan istifadə edərək sorğunu qururuq
    # SQL injection-dan qorunmaq və mətni düzgün oxumaq üçün '{}' dırnaq daxilində yazılmalıdır
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC".format(sys.argv[4])
    
    cursor.execute(query)
    
    # Nəticələri ekrana çıxarırıq
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    # Bağlantıları bağlayırıq
    cursor.close()
    db.close()