import sqlite3
from flask import Flask

def get_db():
  db = getattr(Flask, '_database', None)
  if sb is None:
    db = Flask._database = sqlite3.connect('./room-share-data.sqlite')
  return db

@app.route()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()