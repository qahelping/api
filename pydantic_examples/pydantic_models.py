from enum import Enum
from typing import List

from pydantic import BaseModel


class Category(Enum):
    electronics = "electronics"
    food = "food"


class Item(BaseModel):
    name: str
    price: float
    category: Category


class Order(BaseModel):
    order_id: int
    items: List[Item]


order = Order(
    order_id=42,
    items=[{"name": "Phone", "price": 899.99, "category": "electronics"}]
)
order2 = Order(
    order_id=42,
    items=[{"name": "Phone", "price": 899.99, "category": "electronics2"}]
)
print(order)
print(order2)
