import sqlite3
from sqlite3 import Error

# Database setup and helper functions
def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection successful")
    except Error as e:
        print(f"Error: {e}")
    return conn

def create_table(conn):
    """Create the items table if it doesn't already exist."""
    #print('here')
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL
        );
        """
        cursor = conn.cursor()
        #print('here')
        cursor.execute(sql_create_table)
        #print('here 2')
        print("Table created successfully")
    except Error as e:
        print(f"Error: {e}")

def insert_item(conn, item):
    """Insert a new item into the items table."""
    sql_insert = """
    INSERT INTO items (name, description, price) 
    VALUES (?, ?, ?);
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert, (item.name, item.description, item.price))
        conn.commit()
        print("Item added successfully")
    except Error as e:
        print(f"Error: {e}")

def fetch_items(conn):
    """Fetch all items from the items table."""
    sql_select = "SELECT * FROM items"
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select)
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error: {e}")
        return []

def fetch_item_by_id(conn, item_id):
    """Fetch a specific item by its ID."""
    sql_select = "SELECT * FROM items WHERE id = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select, (item_id,))
        row = cursor.fetchone()
        return row
    except Error as e:
        print(f"Error: {e}")
        return None

def update_item(conn, item_id, item):
    """Update an existing item in the items table."""
    sql_update = """
    UPDATE items
    SET name = ?, description = ?, price = ?
    WHERE id = ?;
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_update, (item['name'], item['description'], item['price'], item_id))
        conn.commit()
        print("Item updated successfully")
    except Error as e:
        print(f"Error: {e}")

def delete_item(conn, item_id):
    """Delete an item from the items table."""
    sql_delete = "DELETE FROM items WHERE id = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql_delete, (item_id,))
        conn.commit()
        print("Item deleted successfully")
    except Error as e:
        print(f"Error: {e}")
'''
if __name__ == "__main__":
    # Specify the SQLite database file
    db_file = "items.db"

    # Establish connection and setup the database
    conn = create_connection(db_file)
    if conn:
        create_table(conn)
        conn.close()
'''