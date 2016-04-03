from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import sys

dbname = "TCount"
if(len(sys.argv)>1):
        arg = sys.argv[1]
	limit_l,limit_h = arg.split(",")

	con = connect(user ='postgres', database=dbname, host = 'localhost', password = 'pass', port=5432)
	cur = con.cursor()

	cur.execute(cur.mogrify("Select * from tweetwordcount where Count>= %s and Count <=%s",(limit_l,limit_h)))

	for row in cur.fetchall():
		print(row)
else:
	print('Missing Count argument')
