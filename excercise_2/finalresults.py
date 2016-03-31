#!/bin/sh

from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import sys 

dbname = "TCount"

#Connecting to database
con = connect(user ='postgres', database=dbname, host = 'localhost', password = 'pass', port=5432)
cur = con.cursor()

word = sys.argv[1]
cur.execute(cur.mogrify("Select * from tweetwordcount where Word = %s",(word,)))
for row in cur.fetchall():
	print(row)

con.commit();
cur.close();
con.close();

#def show_query(title, qry):
#   print('%s' % (title))
#   cur.execute(qry)
#   for row in cur.fetchall():
#       print(row)
#    print('')

#dbname = 'TCount'
#print('connecting to default database ...')
#con = connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
#con = connect(user ='postgres', host = 'localhost', password = '*****', port=5492)
#con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#cur = con.cursor()
#con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#cur.execute('''DROP DATABASE "TCount";''')
#show_query('current database', 'SELECT current_database()')
#cur.execute('CREATE DATABASE ' + dbname)
#show_query('available databases', 'SELECT * FROM pg_database')
#cur.close()
#con.close()

#print('connecting to %s ...' % (dbname))
#con = connect(user ='postgres', database=dbname, host = 'localhost', password = 'pass', port=5432)
#cur = con.cursor()
#ID='5'
#name = 'E\'reader'
#show_query('current database', 'SELECT * from information_schema.tables where table_name=\'Tweetwordcount\'')
#show_query('current database', 'SELECT * from information_schema.tables')
#show_query('current database', "SELECT Word, Count from Tweetwordcount")
#show_query('current database', "DROP TABLE IF EXISTS  Tweetwordcount")
#cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY,NAME VARCHAR(20))")
#cur.execute(cur.mogrify("INSERT INTO Cars VALUES(%s,%s)",(ID,name)))
#cur.execute("TRUNCATE TABLE tweetwordcount")
#show_query('tweetwordcount',"Select * from tweetwordcount order by Count desc LIMIT 10;")
#con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#cur.execute('''DROP DATABASE "TCount";''')
#show_query('cars',"Select * from Cars;")

#con.commit()
#cur.close()
#con.close()

