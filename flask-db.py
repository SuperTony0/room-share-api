import sqlite3

users_table = 'users'

dbConnection = sqlite3.connect('./room-share-data.sqlite')
c = dbConnection.cursor()

c.execute("INSERT INTO users ('first_name', 'last_name', 'email') VALUES ('Tony', 'Goldsmith', 'tony.h.goldsmith@gmail.com')")

dbConnection.commit()
dbConnection.close()