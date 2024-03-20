#!/usr/bin/python3
""" script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa """
import MySQLdb
import sys
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
            SELECT cities.id, cities.name, states.name
            FROM cities LEFT JOIN states
            ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id;
            """
    mycursor.execute(query, (sys.argv[4],))
    cities = mycursor.fetchall()
    for idx in range(len(cities)):
        print(cities[idx][1],
              end=', ' if idx != len(cities) - 1 else '')
    print()
    mycursor.close()
    mydb.close()
