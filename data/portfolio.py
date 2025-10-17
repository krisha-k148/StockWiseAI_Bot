import sqlite3

def init_db():
    conn = sqlite3.connect('user_portfolios.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Create Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    )
    ''')

    # Create Portfolio table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Portfolio (
        portfolio_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        stock_symbol TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        avg_price FLOAT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE
    )
    ''')

    conn.commit()
    conn.close()
    print("✅ Database initialized successfully!")

def get_user_portfolio(user_id):
    conn = sqlite3.connect('user_portfolios.db')
    cursor = conn.cursor()
    cursor.execute('SELECT stock_symbol, avg_price FROM Portfolio WHERE user_id = ?', (user_id,))
    data = cursor.fetchall()
    conn.close()
    return data

if __name__ == "__main__":
    init_db()

    