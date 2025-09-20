from pydantic import BaseModel

class product_schema(BaseModel):
    name: str
    price: float
    id: int
