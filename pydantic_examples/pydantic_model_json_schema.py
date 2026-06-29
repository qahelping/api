from pydantic import BaseModel, Field

res = "{name: Alice, price: 10, in_stock: true}"


class Product(BaseModel):
    name: str = Field(..., min_length=1)
    price: float = Field(..., gt=0)
    in_stock: bool = True


print(Product.model_json_schema())

json = {'properties': {'name': {'minLength': 1, 'title': 'Name', 'type': 'string'},
                'price': {'exclusiveMinimum': 0, 'title': 'Price', 'type': 'number'},
                'in_stock': {'default': True, 'title': 'In Stock', 'type': 'boolean'}}, 'required': ['name', 'price'],
 'title': 'Product', 'type': 'object'}


j = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "petId": {
      "type": "integer"
    },
    "quantity": {
      "type": "integer"
    },
    "shipDate": {
      "type": "string",
      "format": "date-time"
    },
    "status": {
      "type": "string",
      "enum": ["placed", "shipped", "delivered", "cancelled"]
    },
    "complete": {
      "type": "boolean"
    }
  },
  "required": ["id", "shipDate", "status", "complete"],
  "additionalProperties": false
}


