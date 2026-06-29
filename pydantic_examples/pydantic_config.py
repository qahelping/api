from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str

    class Config:
        str_strip_whitespace = True
        validate_assignment = True
        frozen = True
        extra = "allow"
