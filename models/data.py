from typing import Optional

from pydantic import BaseModel, Field, field_validator


class Order(BaseModel):
    id_: int = Field(alias="id", strict=True)
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: Optional[bool] = None

    @field_validator("id_")
    @classmethod
    def id_must_be_7_chars(cls, value: int):
        if len(str(value)) < 7:
            raise ValueError("ID less than 7 chars")
        return value

