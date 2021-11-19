#!/usr/bin/python
import psycopg
from config import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()
        print('Params ', params)
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg.connect(**params)

        # create a cursor
        cur = conn.cursor()

	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT * from votes')
        # display the PostgreSQL database server version
        db_version = cur.fetchall()

        print("Print columns values")
        for row in db_version:
            print( row[0] )

        flat_list = []
        for row in db_version:
            flat_list.append(row[0])

        print("flat_list")
        print(flat_list)

        print(db_version)



	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()