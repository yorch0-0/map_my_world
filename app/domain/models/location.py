from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.domain.models.category import Category


class BaseLocation(BaseModel):
    id: Optional[UUID]
    name: str
    latitude: float
    longitude: float
    category_id: UUID


class Location(BaseLocation):
    category: Category
    reviews: list
