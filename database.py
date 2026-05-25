import sqlite3
import csv
import os
from datetime import datetime

def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input TEXT,
        category TEXT,
        recommendation TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()

def insert_data(user_input, category, recommendation):
    # Simpan ke SQLite
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO history (input, category, recommendation)
    VALUES (?, ?, ?)
    """, (user_input, category, recommendation))

    conn.commit()
    conn.close()

    # Simpan juga ke CSV
    csv_file = "data.csv"
    file_exists = os.path.isfile(csv_file)
    
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Input', 'Category', 'Recommendation', 'Timestamp'])
        writer.writerow([user_input, category, recommendation, datetime.now()])