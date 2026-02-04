import sqlite3
import os

try:
    conn = sqlite3.connect('movies.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM movies')
    rows = cursor.fetchall()
    with open('db_check.txt', 'w') as f:
        f.write(f"Found {len(rows)} rows.\n")
        for row in rows:
            f.write(f"ID: {row['id']}, Title: {row['title']}\n")
    conn.close()
    print("Check complete.")
except Exception as e:
    with open('db_check.txt', 'w') as f:
        f.write(f"Error: {e}\n")
