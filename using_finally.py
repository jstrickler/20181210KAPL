#!/usr/bin/env python

import sqlite3

conn = None

try:
    conn = sqlite3.connect('/Users/jstrick/py/DATA/presidents.db')
    cur = conn.cursor()
    cur.execute("select firstname, lastname from presidents")
    for row in cur.fetchall():
        print(row)
except sqlite3.DatabaseError as err:
    print(err)
    exit()
finally:
    print("Closing!")
    if conn is not None:
        conn.close()
