from uuid import UUID

from pydantic import BaseModel


class CreateReviewDTO(BaseModel):
    location_id: UUID
    rate: int
