""" I think this is where I should put this code for the DB-API"""

# Step 1 Define your Connection Characteristics
dbconfig = { 'host': '127.0.0.1',
             'user': 'vsearch',
             'password': 'ok',
             'database': 'vsearchlogDB2',}

# Step 2 Import your DB Driver
import mysql.connector
# makes the MySQL specific driver available to the DB-API

# Step 3 Establish a connection to server
conn = mysql.connector.connect(**dbconfig)
# call connect establishes the connection argument with the dicitonary above

# Step 4 Open a cursor
cursor = conn.cursor()
#cursor can send commands to the server and receive results

# Step 5 Do the SQL
_SQL = """show tables""" #use _varname and """ for queries
cursor.execute(_SQL)

res = cursor.fetchall()# retrieves all the results from query

"""a different query"""

_SQL_two = """describe log"""
cursor.execute(_SQL_two)
res = cursor.fetchall()

for row in res:
    print(row)

"""and another"""

_SQL_three = """insert into log
                (phrase, letters, ip, browser_string, results)
                values
                (%s, %s, %s, %s, %s)"""

cursor.execute(_SQL_three, ('some_phrase', 'someletters', '127.0.0.1', 'Firefox', 'set()'))

""" an expensive way to force a commit to bypass the cache system"""

conn.commit()#forces it to be written to table
_SQL_four = """select * from log"""
cursor.execute(_SQL_four)       #retrieves
for row in cursor.fetchall():   #just written
    print(row)                  #data
    
