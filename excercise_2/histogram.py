from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import sys
import matplotlib.pyplot as plt

dbname = "TCount"

#Connecting to database
con = connect(user ='postgres', database=dbname, host = 'localhost', password = 'pass', port=5432)
cur = con.cursor()

plt.bar(range(0,100), x)
plt.show()
