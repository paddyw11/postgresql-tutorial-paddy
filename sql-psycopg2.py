import psycopg2

# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Query 1 - select all the records from the "Artist Table"
#cursor.execute('SELECT * FROM "artist"')

# Query2  - select only the "name" column from the "Artist Table"
#cursor.execute('SELECT "name" FROM "artist"')

# query 3 - select only "queen" from the "artist" table
#cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["U2"] )

# query 4 - select only "queen" from the "artist" table
#cursor.execute('SELECT * FROM "artist" WHERE "name" = %s', ["U2"] )

# query 5 - select only "queen" from the "artist" table
#cursor.execute('SELECT * FROM "album" WHERE "artist_id" = %s', [150] )

# query 6 - select only "queen" from the "artist" table
cursor.execute('SELECT * FROM "track" WHERE "composer" = %s', ["test"] )

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
#results = cursor.fetchone()

# close the connection
connection.close()

# print resutls
for result in results:
    print (result)



