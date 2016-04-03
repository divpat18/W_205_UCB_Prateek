from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()
        conn = connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur=conn.cursor()
        
	#Check if database exists. Create if it doesnt.
	cur.execute("select * from pg_database where datname = 'TCount'")
        answer = cur.fetchall()
        if len(answer) > 0:
                self.log("Database already exists");
        else:
                cur.execute('''CREATE DATABASE "TCount";''')
		self.log("Database created!")	
	conn.commit()
        cur.close();
        conn.close;

	#Check if the table exists. Create if it doesnt.
	dbname = 'TCount'	
	conn = connect(database=dbname,user="postgres", password="pass", host="localhost", port="5432")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur=conn.cursor()

        cur.execute("select * from information_schema.tables where table_name='tweetwordcount' ")
        tab_exist = cur.fetchall()
        if(len(tab_exist)>0):
		self.log("Table already exists")
	else:
		cur.execute("CREATE TABLE tweetwordcount (Word TEXT PRIMARY KEY     NOT NULL, Count INT     NOT NULL);")
        conn.commit()
        cur.close();
        conn.close;

    def process(self, tup):
        word = tup.values[0]

	dbname = 'TCount'
	conn = connect(database=dbname,user="postgres", password="pass", host="localhost", port="5432")
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur=conn.cursor()
        
	# Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])
	cur.execute(cur.mogrify("Select * from tweetwordcount  where Word = %s;",(word,)));
	wordcount= cur.fetchall()
	if(len(wordcount)>0):
		cur.execute(cur.mogrify("UPDATE tweetwordcount SET Word = %s,Count=%s WHERE Word = %s;",(word,self.counts[word],word)))
	else:
		cur.execute(cur.mogrify("INSERT INTO tweetwordcount VALUES(%s,%s);",(word,self.counts[word])))

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
