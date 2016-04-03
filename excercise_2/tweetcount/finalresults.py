from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import sys 

dbname = "TCount"

#Connecting to database
con = connect(user ='postgres', database=dbname, host = 'localhost', password = 'pass', port=5432)
cur = con.cursor()

if(len(sys.argv)>1):
	word = sys.argv[1]
	cur.execute(cur.mogrify("Select * from tweetwordcount where Word = %s",(word,)))
	for row in cur.fetchall():
		print(row)
else:
	cur.execute("Select * from tweetwordcount")
	for row in cur.fetchall():
                print(row)


con.commit();
cur.close();
con.close();
