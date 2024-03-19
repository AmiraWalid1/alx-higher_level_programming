#!/usr/bin/python3
''' script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument. '''
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
    mycursor.execute(
                    """
                    SELECT * FROM states
                    WHERE name = '{}'
                    ORDER BY id
                    """.format(sys.argv[4])
                    )
    states = mycursor.fetchall()
    for record in states:
        print(record)
    mycursor.close()
    mydb.close()
