# **FastAPI Practice Project - API Development**

This repository is a **practice project** aimed at learning and mastering API development using **FastAPI**, a modern, fast (high-performance) Python framework for building APIs. The ultimate goal is to develop a reusable, well-structured API **template** that can be quickly cloned, adapted, and deployed for various projects.

---

## **Project Overview**

This API is designed to serve as a foundational template for future development projects. It follows best practices in:

- **Framework**: FastAPI  
- **Language**: Python  
- **Database**: SQLite (with potential integration with PostgreSQL or MySQL)  
- **Frontend**: Potential integration with React for full-stack development  
- **Versioning**: Iterative versioning (`V0`, `V0a`, `V1`, etc.), allowing for incremental improvements.

Each version focuses on refining functionality, code organization, performance, and scalability. The final product will act as a **go-to API template** for rapid deployment and customization.

---

## **Features**

### **Current Functionality**
1. **CRUD Operations**:
   - Perform Create, Read, Update, and Delete operations on items stored in a SQLite database.
   - Available endpoints:
     - `GET /items`: Retrieve all items.
     - `GET /items/{item_id}`: Retrieve a specific item by ID.
     - `POST /items/`: Add a new item.
     - `PUT /items/{item_id}`: Update an existing item.
     - `DELETE /items/{item_id}`: Remove an item.

2. **Input Validation**:
   - Pydantic models ensure robust validation of input data:
     ```python
     class Item(BaseModel):
         name: str = Field(..., min_length=1, max_length=50)
         description: str = Field(default="", max_length=200)
         price: float = Field(..., ge=0)
     ```

3. **Database Connection Management**:
   - Efficient database handling using dependency injection:
     ```python
     def get_db_connection():
         conn = create_connection(db_file)
         try:
             yield conn
         finally:
             conn.close()
     ```

4. **Error Handling**:
   - Provides meaningful HTTP status codes and error messages for client-side and server-side issues:
     ```python
     raise HTTPException(status_code=404, detail="Item not found")
     ```

5. **Interactive Documentation**:
   - Automatically generated Swagger UI (`/docs`) and ReDoc (`/redoc`) for exploring and testing API endpoints.

---

## **Setup Instructions**

### **Prerequisites**
1. **Python 3.10+**  
2. **Virtual Environment**: Use `venv` or similar tools for dependency management.  
3. **Node.js and npm** (optional for React frontend).

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   
2. Set up a virtual environment:
   ```python
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate     # Windows

3. Install dependencies:
   ```bash
    pip install -r requirements.txt

4. Run the application:
    ```bash
    uvicorn src.main:app --reload

### Not complete
Visit the interactive documentation:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc

5. Directory Structure
API_V1/
├── src/                    # FastAPI backend code
│   ├── main.py             # Main application file
│   ├── db/                 # Database-related code
│   │   ├── db_items.py     # CRUD operations for the database
│   └── schemas/            # Pydantic models (future modularization)
├── venv/                   # Virtual environment
├── frontend/               # React frontend code (future integration)
└── README.md               # Project documentation


### **Future Plans & Short-Term Goals** ###

### **Short-Term Goals ###

1. **Frontend Integration**
   - Build a React frontend for interacting with the API.

   **Features**:
   - Display all items.
   - Add, update, and delete items.

2. **Enhance Validation**
   - Add custom validation logic for more complex use cases.

3. **Add Unit Tests**
   - Use `pytest` for backend testing.
   - Validate endpoints and database operations.

---

### **Long-Term Goals**

4. **Scalability**
   - Transition from SQLite to PostgreSQL or MySQL for production environments.
   - Implement connection pooling with SQLAlchemy or asyncpg.

5. **Deployment**
   - Deploy the API using Docker for containerized environments.
   - Host on platforms like AWS, Azure, or Google Cloud.

6. **Authentication**
   - Add user authentication and authorization using OAuth2 or JWT.

7. **Performance Optimization**
   - Enable asynchronous database queries.
   - Profile and optimize API response times.

8. **Versioning**
   - Each version (V0, V0a, V1, etc.) represents:
     - Incremental improvements in functionality.
     - Experimentation with new features and practices.
     - A step toward creating a reusable API template.

---

### **Technologies Used**

9. **Backend**
   - FastAPI, Python

10. **Database**
    - SQLite (with migration plans for PostgreSQL/MySQL)

11. **Frontend (Planned)**
    - React, Axios

12. **Testing (Planned)**
    - pytest

13. **Documentation**
    - FastAPI’s built-in Swagger UI and ReDoc

14. **Deployment (Planned)**
    - Docker, AWS, or similar platforms

---

### **Contributing**
15. Feel free to fork this repository and experiment with it.  
    Pull requests with improvements or suggestions are welcome!
