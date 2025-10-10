import sqlite3

# Connect to database (or create if it doesn't exist)
conn = sqlite3.connect('user_portfolios.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password_hash TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Portfolio (
    portfolio_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    stock_symbol TEXT,
    quantity INTEGER,
    avg_price FLOAT,
    FOREIGN KEY(user_id) REFERENCES Users(user_id)
)
''')

conn.commit()
conn.close()