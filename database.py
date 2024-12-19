import sqlite3

def connect_db():
    """Connect to SQLite database."""
    return sqlite3.connect('meal_planner.db')

def create_tables():
    """Create the database tables if they do not exist."""
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create Recipes Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS recipes (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        instructions TEXT NOT NULL)''')
    
    # Create Ingredients Table
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        quantity TEXT NOT NULL,
                        recipe_id INTEGER,
                        FOREIGN KEY (recipe_id) REFERENCES recipes(id))''')
    
    conn.commit()
    conn.close()
