from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from dependencies.db import get_db_connection
from models.item import Item
from db.db_items import fetch_items, fetch_item_by_id, insert_item, update_item, delete_item

router = APIRouter()

@router.get("/")
def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the API"}

@router.get("/items")
def get_items(conn=Depends(get_db_connection)):
    """Retrieve all items."""
    items = fetch_items(conn)
    items = [Item(name=item[1], description=item[2], price=item[3]).dict() for item in items]
    return JSONResponse(status_code=200, content=items)

@router.get("/items/{item_id}")
def read_item(item_id: int, conn=Depends(get_db_connection)):
    """Retrieve a single item by ID."""
    item = fetch_item_by_id(conn, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    item = Item(name=item[1], description=item[2], price=item[3]).dict()
    return JSONResponse(status_code=200, content=item)

@router.post("/items/")
def create_item(item: Item, conn=Depends(get_db_connection)):
    """Create a new item."""
    insert_item(conn, item)
    return {"message": "Item created successfully", "item": item.model_dump()}

@router.put("/items/{item_id}")
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

@router.delete("/items/{item_id}")
def nuke_item(item_id: int, conn=Depends(get_db_connection)):
    """Delete an item."""
    item = fetch_item_by_id(conn, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    delete_item(conn, item_id)
    return JSONResponse(status_code=204, content={"message": f"Item {item_id} deleted"})
