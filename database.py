import sqlite3
import pandas as pd
import os

DB_NAME = "movies.db"

def get_connection():
    """Establishes a connection to the SQLite database."""
    conn = sqlite3.connect(DB_NAME)
    # This allows accessing columns by name: row['title']
    conn.row_factory = sqlite3.Row
    return conn

def setup_db():
    """Creates the movies table if it doesn't already exist."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # We use 'id' as the primary key from the API to avoid duplicates.
    # Note: We use JSON to store the full movie data if needed, or specify columns.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            release_date TEXT,
            runtime INTEGER,
            budget INTEGER,
            revenue INTEGER,
            vote_average REAL,
            popularity REAL,
            vote_count INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def save_movie(movie_data):
    """Inserts or updates a movie in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    
    # Using 'INSERT OR REPLACE' (Upsert) to handle updates if the movie already exists.
    cursor.execute('''
        INSERT OR REPLACE INTO movies (
            id, title, release_date, runtime, budget, revenue, vote_average, popularity, vote_count
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        movie_data.get('id'),
        movie_data.get('title'),
        movie_data.get('release_date'),
        movie_data.get('runtime'),
        movie_data.get('budget'),
        movie_data.get('revenue'),
        movie_data.get('vote_average'),
        movie_data.get('popularity'),
        movie_data.get('vote_count')
    ))
    
    conn.commit()
    conn.close()

def save_movies_batch(movies_list):
    """Saves a list of movies to the database."""
    for movie in movies_list:
        save_movie(movie)

def get_movies_batch():
    """Gets a list of movies from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    res = cursor.execute('''
        SELECT * FROM movies
    ''')
    rows = res.fetchall()
    print(len(rows))
    df = pd.read_sql_query("SELECT * FROM movies", conn)
    print(df.head(n=50))
    conn.close()

def delete_db():
    """Deletes all movies from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM movies''')
    conn.commit()
    cursor.execute('''
        SELECT COUNT(*) FROM movies
    ''')
    result = cursor.fetchone()
    num_rows = result[0]
    print(num_rows)
    conn.close()
if __name__ == "__main__":
    get_movies_batch()

