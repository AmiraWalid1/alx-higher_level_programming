#!/usr/bin/python3
''' script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument '''
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
    query = """
            SELECT * FROM states
            WHERE name LIKE BINARY %s
            ORDER BY id
        """
    mycursor.execute(query, (sys.argv[4],))
    states = mycursor.fetchall()
    for record in states:
        print(record)
    mydb.commit()
    mycursor.close()
    mydb.close()
