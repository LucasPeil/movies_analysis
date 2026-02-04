import database
import sqlite3
import os

def test_database():
    print("Starting database verification...")
    
    # 1. Setup DB
    database.setup_db()
    if os.path.exists("movies.db"):
        print("Success: movies.db created.")
    else:
        print("Failure: movies.db not found.")
        return

    # 2. Save a test movie
    test_movie = {
        'id': 123,
        'title': 'Test Movie',
        'overview': 'This is a test movie overview.',
        'release_date': '2024-01-01',
        'vote_average': 8.5,
        'popularity': 100.0,
        'vote_count': 10
    }
    database.save_movie(test_movie)
    print("Success: Test movie saved.")

    # 3. Verify content
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE id = 123")
    row = cursor.fetchone()
    conn.close()

    if row and row['title'] == 'Test Movie':
        print(f"Success: Retrieved movie '{row['title']}' from database.")
    else:
        print("Failure: Could not retrieve test movie correctly.")

if __name__ == "__main__":
    test_database()
