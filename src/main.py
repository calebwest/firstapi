from fastapi import FastAPI, Body as body
from pydantic import BaseModel, Field
from db.db_items import insert_item, create_connection, create_table, fetch_items, fetch_item_by_id, update_item, delete_item

# Create FastAPI instance
app = FastAPI()
db_file = "items.db"

# Create connection and setup the database at app startup
@app.on_event("startup")
def on_startup():
    conn = create_connection(db_file)
    if conn:
        create_table(conn)  # Create the table if it doesn't exist
        conn.close()

class Item(BaseModel):
    name: str = Field()
    description: str = Field()
    price: float = Field()

###########################
# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI application!"}
@app.get("/items")
def get_items():
    conn = create_connection(db_file)
    return fetch_items(conn)

# Example endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Retrieve an item by its ID and optionally include a query string parameter.
    """
    conn = create_connection(db_file)
    return fetch_item_by_id(conn,item_id)

# Example endpoint for creating an item
@app.post("/items/")
def create_item(item: Item = body(...)):
    """
    Create a new item and return its details.
    """
    conn = create_connection(db_file)
    insert_item(conn, item)
    conn.close()  # Ensure the connection is closed after use
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
    }

@app.put("/items/{item_id}")
def put_item(item_id: int, item: Item = body(...)):
    '''
    Update an item by its ID
    '''
    conn = create_connection(db_file)
    updated_item = {
        "name": item.name,
        "description": item.description,
        "price": item.price,
    }
    update_item(conn, item_id, updated_item)
    updated_item["item_id"] = item_id
    return updated_item

@app.delete("/items/{item_id}")
def nuke_item(item_id):
    '''
    Update an item by its ID
    '''
    conn = create_connection(db_file)
    delete_item(conn, item_id)
    return


###########################

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)






##########################################################
#OG
##########################################################
'''from fastapi import FastAPI, Body as body
from pydantic import BaseModel, Field
from db.db_items import insert_item, create_connection, create_table

# Create FastAPI instance
app = FastAPI()
db_file = "items.db"
class Item(BaseModel):
    name: str = Field()
    description: str = Field()
    price: float = Field()

###########################
# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI application!"}

# Example endpoint
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Retrieve an item by its ID and optionally include a query string parameter.
    """
    return {"item_id": item_id, "q": q}

# Example endpoint for creating an item
@app.post("/items/")
def create_item(item: Item=body(...)):
    """
    Create a new item and return its details.
    """
    # ln 50 closes db - this reopens db
    conn = create_connection(db_file)
    insert_item(conn,item)
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
    }
###########################

if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080) # local host - uvicorn main:app --host 127.0.0.1 --port 8080 --reload # port:8000 was likely taken up by other prgm

    # Establish connection and setup the database
    conn = create_connection(db_file)
    print(conn)
    if conn:
        create_table(conn)
        conn.close()
'''