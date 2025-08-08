from uuid import UUID

from pydantic import BaseModel


class CreateLocationDTO(BaseModel):
    name: str
    latitude: float
    longitude: float
    category_id: UUID
