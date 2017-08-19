import sqlite3

dbConnection = sqlite3.connect('./room-share-data.sqlite')
c = dbConnection.cursor()

people = c.execute('SELECT * from users')

print people

dbConnection.commit()
dbConnection.close()