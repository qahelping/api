from datetime import datetime

from pydantic import BaseModel
from pydantic import ValidationError


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None


res_data = {"id": "123", "name": "Alice", "signup_ts": "2025-09-22 10:15"}

user: User = User(**res_data)

print(user.id, type(user.id))  # 123 <class 'int'>
print(user.signup_ts, type(user.signup_ts))  # datetime объект


res_data_error_types = {"id": "abs", "name": 123}
res_data_error_field = {"id": "1"}


try:
    u1 = User(id="abc", name=123)
except ValidationError as e:
    print('1: ', e)

try:
    u2 = User(**res_data_error_types)
except ValidationError as e:
    print('2: ', e)

try:
    u3 = User(**res_data_error_field)
except ValidationError as e:
    print('3: ', e)