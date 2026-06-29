import requests
from pydantic import HttpUrl, BaseModel, Field

# class Shema:
#     height: int
#     floors: int = 10
#     id_: int
#     address: str
#
#     def __init__(self, height):
#         self.height = height
#
#     def change_floors(cls, floors):
#         cls.floors = floors
#
# class Pet:
#     id_: int
#     name: str
#     type_of_pet = ['cat', 'dog']
#
# milka = Pet(1, 'Milka', 'cat')
# jyja = Pet(2, 'Jyja', 'dog')
#

r = requests.get('https://api.thecatapi.com/v1/images/search?limit=1')
data = r.json()
print(data)

class Image(BaseModel):
    id: str
    url: HttpUrl
    width: int = Field(..., ge=0, le=1000)
    height: int = Field(..., ge=0, le=1000)

for image_item in data:
    image = Image(**image_item)
    print(image)

