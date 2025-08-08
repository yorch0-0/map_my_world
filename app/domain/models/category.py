from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Category(BaseModel):
    id: Optional[UUID]
    name: str