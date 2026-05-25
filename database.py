import sqlite3

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input TEXT,
        category TEXT,
        recommendation TEXT
    )
    """)

    conn.commit()
    conn.close()

def insert_data(user_input, category, recommendation):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history (input, category, recommendation)
    VALUES (?, ?, ?)
    """, (user_input, category, recommendation))

    conn.commit()
    conn.close()