from pydantic import BaseModel


class ImageRequestSchema(BaseModel):
    id: int
    prompt: str


class ImageSchema(BaseModel):
    id: int
    img: str
