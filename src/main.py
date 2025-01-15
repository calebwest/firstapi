from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
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

# Database connection dependency (update from V0 where connection was created repeatedly)
def get_db_connection():
    """
    Dependency to provide a database connection.
    Automatically closes the connection after use.
    """
    conn = create_connection(db_file)
    try:
        yield conn  # Provide the connection to the endpoint
    finally:
        conn.close()

# Schema with limits
class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    description: str = Field(default="", max_length=200)
    price: float = Field(..., ge=0)

###########################

# Connection prompt (revise comment)
@app.get("/")
def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the API"}

# Endpoint  - get all items
@app.get("/items")
def get_items(conn=Depends(get_db_connection)):
    """Retrieve all items."""
    items=fetch_items(conn)
    items=[Item(name=item[1],description=item[2],price=item[3]).dict() for item in items]
    return JSONResponse(status_code=200, content=items)

# Endpoint - Read item
@app.get("/items/{item_id}")
def read_item(item_id: int, conn=Depends(get_db_connection)):
    """Retrieve a single item by ID."""
    item=fetch_item_by_id(conn, item_id)
    item=Item(name=item[1],description=item[2],price=item[3]).dict()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return JSONResponse(status_code=200, content=item)

# Endpoint - Create item
@app.post("/items/")
def create_item(item: Item, conn=Depends(get_db_connection)):
    """Create a new item."""
    insert_item(conn, item)
    return {"message": "Item created successfully", "item": item.model_dump()}

# Endpoint - Update item
@app.put("/items/{item_id}")
def put_item(item_id: int, item: Item, conn=Depends(get_db_connection)):
    """Update an existing item."""
    existing_item = fetch_item_by_id(conn, item_id)
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")
    updated_item = {
        "name": item.name,
        "description": item.description,
        "price": item.price,
    }
    update_item(conn, item_id, updated_item)
    return {"message": "Item updated successfully", "item": updated_item}

# Endpoint - Delete item
@app.delete("/items/{item_id}")
def nuke_item(item_id: int, conn=Depends(get_db_connection)):
    """Delete an item."""
    item = fetch_item_by_id(conn, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_item(conn, item_id)
    return JSONResponse(status_code=204, content={"message": f"Item {item_id} deleted"})


###########################
# Main (8000 port taken, used 8080)
if __name__ == "__main__":
    import uvicorn

    # Run the FastAPI application using uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)

