from fastapi import FastAPI
from api.endpoints import router as item_router
from db.db_items import create_connection, create_table

# Create FastAPI instance
app = FastAPI()

db_file = "items.db"

@app.on_event("startup")
def on_startup():
    conn = create_connection(db_file)
    if conn:
        create_table(conn)  # Create the table if it doesn't exist
        conn.close()

# Include the item endpoints
app.include_router(item_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)

