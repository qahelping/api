import re
from ipaddress import IPv4Address

from pydantic import BaseModel, constr, ValidationError, AnyUrl, HttpUrl, conlist, field_validator
from pydantic.v1 import PositiveInt, UUID1


class User(BaseModel):
    id: int
    name: str
    age: int | None = None
    type: str | None = 'Human'


alice1 = User(id=1, name="Alice")
alice = User(id=1, name="Alice", type='Child')

#  явное указание обязательного поля и ограничений
from pydantic import BaseModel, Field


class Product(BaseModel):
    name: str = Field(..., description="Название продукта")
    price: float = Field(..., gt=0)


#  необязательные поля
from typing import Optional


class Profile(BaseModel):
    username: str
    bio: Optional[str] = None


# валидация

from pydantic import BaseModel, Field

response = {'id': 1, 'age': 20, 'url': 'https://example.com', 'namePet': 'Alice', 'email': "email@gmail.com"}

class User(BaseModel):
    id_: int =  Field(..., gt=0, alias='id')
    age: int = Field(..., ge=18, le=99)  # >=18 и <=99
    name_pet: str = Field(..., min_length=2, max_length=50, alias='namePet')
    email: str
    url: Optional[str] = None

    @field_validator("email")
    @classmethod
    def check_email(cls, v):
        if not re.match(r'^\S+@\S+\.\S+$', v):
            raise ValueError("Некорректный email")
        return v

user = User(**response)
print('user: ', user)

# готовый тип EmailStr
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    email: EmailStr
    url: AnyUrl
    http_url: HttpUrl
    ip: IPv4Address
    pos: PositiveInt
    uuid: UUID1


# пример корректных данных
valid_data = {
    "age": 25,
    "name": "Elena",
    "email": "elena@example.com"
}
user = User(**valid_data)
print(user)
# print("Корректный объект:", user.model_dump())

# # пример ошибок
# invalid_data = {
#     "age": 15,
#     "name": "A",
#     "email": "not-an-email.com"
# }
#
# try:
#     User(**invalid_data)
# except ValidationError as e:
#     assert False, f'Test failed. {e}'
#     print("Ошибки валидации:", e)
#
#
# class User(BaseModel):
#     id_: int =  Field(..., gt=0, alias='id')
#     age: int = Field(..., gt=18, le=99)  # >=18 и <=99
#     name_pet: str = Field(..., min_length=2, max_length=50, alias='namePet')
#     email: constr(pattern=r'^\S+@\S+\.\S+$')
#     tags: conlist(str, min_length=1, max_length=10)
#     url: Optional[str] = None