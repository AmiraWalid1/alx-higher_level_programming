#!/usr/bin/python3
''' script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa '''
import sys
import MySQLdb

if __name__ == "__main__":
    mydb = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    mycursor = mydb.cursor()
    mycursor.execute("""
                    SELECT * FROM states
                    WHERE name REGEXP '^N.*'
                    ORDER BY states.id
                    """)
    states = mycursor.fetchall()
    for record in states:
        print(record)
    mycursor.close()
    mydb.close()
