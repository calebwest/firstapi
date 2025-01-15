import sqlite3
from sqlite3 import Error

# Database setup and helper functions
def create_connection(db_file: str):
    """Create a connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error: {e}")
    return None

#
def create_table(conn):
    """Create the items table if it doesn't already exist."""
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        price REAL NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_table)
        conn.commit()
    except Error as e:
        print(f"Error creating table: {e}")

# 
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

# 
def fetch_items(conn):
    """Fetch all items from the items table."""
    sql_select = "SELECT * FROM items"
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select)
        return cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
        return []

#
def fetch_item_by_id(conn, item_id):
    """Fetch a specific item by its ID."""
    sql_select = "SELECT * FROM items WHERE id = ?"
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select, (item_id,))
        row = cursor.fetchone()
        return row  # Same here; format in `main.py` if needed
    except Error as e:
        print(f"Error: {e}")
        return None

#
def update_item(conn, item_id, item):
    """Update an existing item."""
    try:
        sql_update = """
        UPDATE items
        SET name = ?, description = ?, price = ?
        WHERE id = ?;
        """
        cursor = conn.cursor()
        cursor.execute(sql_update, (item["name"], item["description"], item["price"], item_id))
        conn.commit()
    except Error as e:
        print(f"Error updating item: {e}")

#
def delete_item(conn, item_id):
    """Delete an item from the items table."""
    try:
        sql_delete = "DELETE FROM items WHERE id = ?"
        cursor = conn.cursor()
        cursor.execute(sql_delete, (item_id,))
        conn.commit()
    except Error as e:
        print(f"Error deleting item: {e}")