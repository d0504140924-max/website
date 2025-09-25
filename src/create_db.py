import sqlite3

def create_db(path):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS products (
    id TEXT PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    manufacturer TEXT NOT NULL,
    price INTEGER NOT NULL,
    cost INTEGER NOT NULL,
    )
                """)

    cur.execute("""
     CREATE TABLE IF NOT EXISTS inventory(
         product_id TEXT PRIMARY KEY NOT NULL,
         amount INTEGER NOT NULL DEFAULT 0,
         )
                 """)

    conn.commit()
    conn.close()







