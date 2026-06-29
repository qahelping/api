import re

from pydantic import BaseModel, field_validator
from pydantic import constr, ValidationError


class Product(BaseModel):
    price: float

    @field_validator("price")
    def positive_price(cls, v):
        if v <= 0:
            raise ValueError("Цена должна быть > 0")
        return v


from pydantic import BaseModel, model_validator


class Booking(BaseModel):
    start: int
    end: int

    @model_validator(mode="after")
    def check_dates(self):
        if self.start >= self.end:
            raise ValueError("start должен быть раньше end")
        return self


# валидация

from pydantic import BaseModel, Field


class User(BaseModel):
    age: int = Field(..., ge=18, le=99)  # >=18 и <=99
    name: str = Field(..., min_length=2, max_length=50)
    email: constr(pattern=r'^\S+@\S+\.\S+$')

    @field_validator("email")
    def check_email(cls, v):
        if not re.match(r'^\S+@\S+\.\S+$', v):
            raise ValueError("Некорректный email")
        return v


# пример корректных данных
valid_data = {
    "age": 25,
    "name": "Elena",
    "email": "elena@example.com"
}
user = User(**valid_data)
print("Корректный объект:", user.model_dump())

