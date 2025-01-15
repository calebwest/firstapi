from db.db_items import create_connection

db_file = "items.db"

def get_db_connection():
    """
    Dependency to provide a database connection.
    Automatically closes the connection after use.
    """
    conn = create_connection(db_file)
    try:
        yield conn
    finally:
        conn.close()
