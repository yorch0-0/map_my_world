from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

from app.domain.models.location import Location


class BaseReview(BaseModel):
    id: Optional[UUID]
    rate: int
    location_id: UUID
    created_at: datetime


class Review(BaseReview):
    location: Location
