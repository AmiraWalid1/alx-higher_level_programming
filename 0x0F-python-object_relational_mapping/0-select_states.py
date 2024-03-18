#!/usr/bin/python3
import sys
import MySQLdb
''' script that lists all states from the database hbtn_0e_0_usa '''
if __name__ == "__main__":
    mydb = MySQLdb.connect(
    host='localhost',
    port=3306,
    user=sys.argv[1],
    password=sys.argv[2],
    database=sys.argv[3]
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY states.id")

    for record in mycursor:
        print(record)
