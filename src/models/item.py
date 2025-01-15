from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    description: str = Field(default="", max_length=200)
    price: float = Field(..., ge=0)
