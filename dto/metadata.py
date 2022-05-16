from pydantic import BaseModel


class MetaData(BaseModel):
    name: str
    description: str
