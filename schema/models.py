from pydantic import BaseModel, HttpUrl, Field


class ProductSchema(BaseModel):
    id: int
    name: str = Field(min_length=1)
    price: float
    category: str
    url: HttpUrl
