import sqlite3
from datetime import datetime

# Initialize the database
def init_db():
    conn = sqlite3.connect("tracker.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      type TEXT,
                      title TEXT,
                      link TEXT,
                      tags TEXT,
                      added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn

def add_entry(entry_type, title, link, tags):
    conn = init_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (type, title, link, tags) VALUES (?, ?, ?, ?)',
                   (entry_type, title, link, ",".join(tags)))
    conn.commit()
    conn.close()

