import sqlite3

# Create a new SQLite database or connect to an existing one
db_path = 'password_manager.db'
conn = sqlite3.connect(db_path)

# Create a table to store passwords
create_table_query = '''
CREATE TABLE IF NOT EXISTS passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
'''

# Execute the query
conn.execute(create_table_query)
conn.commit()
conn.close()
